{
    "name": "Owl Welcome",
    "version": "18.0.1.0.0",
    "category": "Website",
    "summary": """EJERCICIO 0  Campus Cleverit
    Componente de vienvenida OWL Basico""",
    "author": "Odoo S.A., Tecnativa",
    "website": "https://www.odoo.com",
    "license": "LGPL-3",

    "depends": ["base","web","contacts"],
    "data": [
        "views/menu_action.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "owl_welcome/static/src/components/welcome_component.js",
            "owl_welcome/static/src/components/welcome_component.xml",
        ],
    },

    "application": True,
}