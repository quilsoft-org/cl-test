# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2021 jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'test11',
    'version': '11.0.1.0.0',
    'category': 'Tools',
    'summary': "Test for v11 CE",
    'author': "jeo Software",
    'website': 'http://github.com/jobiols/module-repo',
    'license': 'AGPL-3',
    'depends': [
        # basic applications
    ],
    'data': [
    ],
    'installable': True,
    'application': False,

    # Here begins odoo-env manifest configuration
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # manifest version, if omitted it is backward compatible but
    # oe will show a deprecation warning
    'env-ver': '2',

    # Configuration data for odoo.conf
    'config': [
    ],

    # Default to CE, can be ommited
    'odoo-license': 'CE',

    # Port where odoo docker image starts serving pages.
    'port': '8069',

    # repositories to be installed in sources/ dir
    # syntax: the same as git clone
    'git-repos': [
        'git@github.com:jobiols/cl-test.git',
        'git@github.com:ingadhoc/odoo-argentina.git',
        'git@github.com:ingadhoc/account-financial-tools.git',
        'git@github.com:ingadhoc/account-invoicing.git',
        'git@github.com:ingadhoc/account-payment.git',
        'git@github.com:ingadhoc/miscellaneous.git',
        'git@github.com:oca/partner-contact.git',
    ],

    # Docker images to be used in this deployment
    # syntax: name url
    'docker-images': [
        'odoo jobiols/odoo-jeo:11.0',
        'postgres postgres:10.1-alpine',
    ]
}
