# controllers/main.py
import logging
import math
import time

import odoo
from odoo import http

_logger = logging.getLogger(__name__)


class PocController(http.Controller):

    def cpu_burn(self, duration=3):
        end_time = time.time() + duration
        while time.time() < end_time:
            # operación matemática inútil pero pesada
            math.sqrt(123456789) ** 5.4321

    @http.route("/poc/process_task", type="jsonrpc", auth="none", csrf=False)
    def process_task(self, **kwargs):

        task_id = kwargs.get("task_id")
        db_name = kwargs.get("db_name")

        with odoo.registry(db_name).cursor() as cr:
            env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
            task = env["hr.tasks"].browse(task_id)

            try:
                # 1. Marcar la tarea como 'generando'
                _logger.info(f"Starting processing for task {task_id} in db {db_name}.")
                task.write({"state": "generating"})
                cr.commit()

                # 2. Simulación de proceso largo

                for ix in range(30):
                    self.cpu_burn(1)
                    _logger.info(
                        f"Processing task {task_id}: {ix + 1}/30 seconds elapsed."
                    )

                # 3. Marcar como finalizada
                task.write({"state": "done"})
                cr.commit()
                _logger.info(f"Task {task_id} processed successfully.")

            except Exception as e:
                _logger.error(f"Error processing task {task_id}: {e}", exc_info=True)
                cr.rollback()
                task.write({"state": "error", "error_message": str(e)})
                cr.commit()
