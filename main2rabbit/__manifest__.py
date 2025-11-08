{
    "name": "Main to RabbitMQ Integration",
    "version": "19.0.1.0.0",
    "author": "Quilsoft",
    "website": "https://www.tuweb.com",
    "category": "Hidden",
    "license": "LGPL-3",
    "depends": [
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_tasks_views.xml",
        "views/hr_tasks_menus.xml",
        "views/rabbitmq_config_data.xml",
    ],
    "installable": True,
    "application": True,
    "external_dependencies": {
        "python": ["pika"],
    },
}
