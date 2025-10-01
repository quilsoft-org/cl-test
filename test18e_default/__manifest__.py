{
    "name": "test18e",
    "version": "18.0.1.0.0",
    "category": "Tools",
    "summary": "Test for v18 OWL",
    "author": "Quilsoft",
        "license": "AGPL-3",
    "depends": [
        "sale",
        ],
    "data": [
        "views/sale_order_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "test18e_default/static/src/components/example.xml",
            "test18e_default/static/src/components/example.js",
        ],
    },


    "env-ver": "2",
    "odoo-license": "EE",
    "config": [
        "workers = 0",
        "admin_password = admin",
    ],
    "port": "8069",
    "git-repos": [
        "https://github.com/quilsoft-org/cl-test.git -b 18.0e-owl",
    ],
    # list of images to use in the form 'name image-url'
    "docker-images": [
        "odoo jobiols/odoo-ent:18.0e",
        "postgres postgres:17.5-alpine",
    ],
}
