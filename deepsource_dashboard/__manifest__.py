{
    "name": "DeepSource Dashboard",
    "version": "17.0.1.0.0",
    "category": "Tools",
    "summary": "Displays DeepSource issues and trend in Odoo",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/deepsource_issue_views.xml",
        "views/deepsource_stat_views.xml",
        "views/deepsource_menu.xml",
        "data/cron.xml"
    ],
    "license": "LGPL-3",
}
