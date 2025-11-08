# URL interna del worker, como discutimos anteriormente
# WORKER_URL = "http://odoo_workers:8069"

import json
import logging

import pika
from odoo import fields, models

_logger = logging.getLogger(__name__)


class HrTasks(models.Model):
    _name = "hr.tasks"
    _description = "Payroll Processing Task"

    # ... (campos como employee_data, state, etc.)
    employee_data = fields.Char(required=True)
    state = fields.Selection(
        [
            ("free", "Sin procesar"),
            ("queued", "En Cola"),
            ("generating", "Generando Nomina"),
            ("done", "Proceso finalizado"),
            ("to_print", "A Imprimir"),
            ("printing", "Imprimiendo"),
            ("finished_print", "Impresion finalizada"),
            ("error", "Error"),
        ],
        default="free",
        index=True,
    )
    error_message = fields.Text(readonly=True)

    def _send_task_to_rabbitmq(self):  # <- NUEVO NOMBRE DEL MÉTODO, más descriptivo
        self.ensure_one()
        if self.state != "free":
            _logger.warning(
                f"Task {self.id} is not in 'free' state, skipping sending to RabbitMQ."
            )
            return

        # 1. Obtener la configuración de RabbitMQ desde los parámetros del sistema
        # Estos se configurarán en __manifest__.py y luego pueden ser modificados en Odoo.
        rabbitmq_host = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("poc_processing_tasks.rabbitmq_host", "rabbitmq")
        )
        rabbitmq_port = int(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("poc_processing_tasks.rabbitmq_port", "5672")
        )
        rabbitmq_user = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("poc_processing_tasks.rabbitmq_user", "user")
        )
        rabbitmq_pass = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("poc_processing_tasks.rabbitmq_pass", "password")
        )
        rabbitmq_queue_name = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("poc_processing_tasks.rabbitmq_queue_name", "payroll_tasks")
        )

        # 2. Preparar el mensaje
        message_payload = {
            "task_id": self.id,
            "db_name": self.env.cr.dbname,
        }
        message_body = json.dumps(message_payload)

        connection = None  # Inicializar a None para el bloque finally
        try:
            # 3. Conectar a RabbitMQ
            credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
            parameters = pika.ConnectionParameters(
                host=rabbitmq_host, port=rabbitmq_port, credentials=credentials
            )
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()

            # 4. Declarar la cola (creará la cola si no existe)
            # durable=True asegura que la cola persista incluso si RabbitMQ se reinicia
            channel.queue_declare(queue=rabbitmq_queue_name, durable=True)

            # 5. Publicar el mensaje
            # delivery_mode=2 marca el mensaje como persistente
            # lo que significa que RabbitMQ lo guardará en disco si la cola es durable
            channel.basic_publish(
                exchange="",  # Usamos el exchange por defecto
                routing_key=rabbitmq_queue_name,  # La clave de enrutamiento es el nombre de la cola
                body=message_body,
                properties=pika.BasicProperties(
                    delivery_mode=2,  # Hacer que el mensaje sea persistente
                ),
            )
            _logger.info(
                f"Task {self.id} message published to RabbitMQ queue '{rabbitmq_queue_name}'."
            )

            # 6. Marcar la tarea en Odoo como 'en cola de RabbitMQ'
            self.write({"state": "queued_rabbitmq"})
            self.env.cr.commit()  # Forzar el commit

        except pika.exceptions.AMQPConnectionError as e:
            _logger.error(
                f"Failed to connect to RabbitMQ for task {self.id}: {e}", exc_info=True
            )
            self.write(
                {"state": "free", "error_message": f"RabbitMQ connection failed: {e}"}
            )
            self.env.cr.commit()
        except Exception as e:
            _logger.error(
                f"Failed to publish task {self.id} to RabbitMQ: {e}", exc_info=True
            )
            self.write(
                {"state": "free", "error_message": f"RabbitMQ publish failed: {e}"}
            )
            self.env.cr.commit()
        finally:
            if connection and connection.is_open:
                connection.close()  # Asegurarse de cerrar la conexión

    def send_tasks_to_worker(self):
        """
        Método llamado por la Acción de Servidor.
        Ahora envía las tareas a RabbitMQ.
        """

        import wdb;wdb.set_trace()
        
        _logger.info(f"Action triggered for tasks: {self.ids}. Sending to RabbitMQ.")
        for task in self:
            task._send_task_to_rabbitmq()
