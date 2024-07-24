##############################################################################
#
#    Copyright (C) 2024
#    All Rights Reserved.
#
##############################################################################

{
    "name": "test17",
    "version": "17.0.1.0.0",
    "category": "Tools",
    "summary": "Test for v17 CE",
    "author": "Quilsoft",
    "website": "http://github.com/jobiols/cl-test",
    "license": "AGPL-3",
    "depends": [],
    "installable": True,
    # manifest version, if omitted it is backward compatible
    "env-ver": "2",
    # if Enterprise it installs in a different directory than community
    "odoo-license": "CE",
    # Config to write in odoo.conf
    "config": [
        "workers = 0",
        "admin_password = admin",
    ],
    "port": "8069",
    "git-repos": [
        "git@github.com:quilsoft-org/cl-test.git",
        "git@github.com:quilsoft-org/addons-private.git"
    ],
    # list of images to use in the form 'name image-url'
    "docker-images": [
        "odoo jobiols/odoo-jeo:17.0",
        "postgres postgres:15.1-alpine",
    ],
}
