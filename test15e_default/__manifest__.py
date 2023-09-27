##############################################################################
#
#    Copyright (C) 2021  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   le agregamos esto
##############################################################################

{
    'name': 'test15e',
    'version': '15.0.1.0.0',
    'category': 'Tools',
    'summary': "Test for v15 CE",
    'author': "jeo Software",
    'website': 'http://github.com/jobiols/cl-test',
    'license': 'AGPL-3',
    'depends': [
        'l10n_ar_ux', # l10n_ar, l10n_latam_check, account_withholding, account_payment_group
        'l10n_ar_edi', # wsfev1 - "Factura Electrónica"
                       # wsbfev1 - "Bono Fiscal Electrónico"
                       # wsfexv1 - "Factura de Exportación Electrónica"
                       # wscdc - "Constatación de Comprobantes"
        'l10n_ar_edi_ux', # bajada de padron
        'l10n_ar_purchase_stock', # l10n_ar_purchase
	    'l10n_ar_account_tax_settlement', # seteo de impuestos para argentina
        'l10n_ar_bank',
        'l10n_ar_account_withholding',

        ],
    'installable': True,

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'EE',

    # Config to write in odoo.conf
    'config': [],

    'port': '8069',

    'git-repos': [
        'https://github.com/jobiols/cl-test.git -b 15.0e',

        # # ingadhoc
        'https://github.com/ingadhoc/odoo-argentina ingadhoc-odoo-argentina',
        'https://github.com/ingadhoc/account-financial-tools ingadhoc-account-financial-tools',
        'https://github.com/ingadhoc/account-invoicing ingadhoc-account-invoicing',
        'https://github.com/ingadhoc/account-payment ingadhoc-account-payment',
        'https://github.com/ingadhoc/odoo-argentina-ee ingadhoc-odoo-argentina-ee',

        'https://github.com/ingadhoc/partner ingadhoc-partner',

        'https://github.com/OCA/brand oca-brand',
        'https://github.com/OCA/partner-contact oca-partner-contact',
        'https://github.com/OCA/server-ux oca-server-ux',
        'https://github.com/OCA/server-tools oca-server-tools',
        'https://github.com/OCA/web oca-web',

	'https://github.com/OCA/commission.git oca-commission',        
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo jobiols/odoo-ent:15.0e',
        'postgres postgres:10.1-alpine',
	'nginx nginx',
    ]
}
