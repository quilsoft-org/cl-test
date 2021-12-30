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
        'standard_depends_ee'
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
        'git@github.com:jobiols/cl-test.git -b 15.0e',

        # OCA
        # 'https://github.com/OCA/l10n-spain.git oca-l10n-spain',
        # 'https://github.com/OCA/server-tools oca-server-tools',
        # 'https://github.com/OCA/stock-logistics-workflow oca-stock-logistics-workflow',
        # 'https://github.com/OCA/sale-workflow oca-sale-workflow',
        # 'https://github.com/OCA/field-service oca-field-service',
        # 'https://github.com/OCA/hr oca-hr',
        # 'https://github.com/OCA/social oca-social',
        # 'https://github.com/OCA/partner-contact oca-partner-contact',
        # 'https://github.com/OCA/pos oca-pos',
        # 'https://github.com/OCA/reporting-engine oca-reporting-engine',
        # 'https://github.com/OCA/hr-expense oca-hr-expense',
        # 'https://github.com/OCA/edi oca-edi',
        # 'https://github.com/OCA/manufacture oca-manufacture',
        # 'https://github.com/OCA/crm oca-crm',
        # 'https://github.com/OCA/purchase-workflow oca-purchase-workflow',
        # 'https://github.com/OCA/project oca-project',
        # 'https://github.com/OCA/search-engine oca-search-engine',
        # 'https://github.com/OCA/maintenance oca-maintenance',
        # 'https://github.com/OCA/stock-logistics-warehouse oca-stock-logistics-warehouse',
        # 'https://github.com/OCA/account-payment oca-account-payment',
        # 'https://github.com/OCA/multi-company oca-multi-company',
        # 'https://github.com/OCA/rma oca-rma',
        # 'https://github.com/OCA/delivery-carrier oca-delivery-carrier',
        # 'https://github.com/OCA/operating-unit oca-operating-unit',
        # 'https://github.com/OCA/knowledge oca-knowledge',
        # 'https://github.com/OCA/wms oca-wms',
        # 'https://github.com/OCA/mis-builder oca-mis-builder',
        # 'https://github.com/OCA/bank-payment oca-bank-payment',
        # 'https://github.com/OCA/account-invoice-reporting oca-account-invoice-reporting',
        # 'https://github.com/OCA/timesheet oca-timesheet',
        # 'https://github.com/OCA/web oca-web',
        # 'https://github.com/OCA/account-financial-tools oca-account-financial-tools',
        # 'https://github.com/OCA/sale-reporting oca-sale-reporting',
        # 'https://github.com/OCA/account-financial-reporting oca-account-financial-reporting',
        # 'https://github.com/OCA/e-commerce oca-e-commerce',
        # 'https://github.com/OCA/contract oca-contract',
        # 'https://github.com/OCA/helpdesk oca-helpdesk',
        # 'https://github.com/OCA/product-attribute oca-product-attribute',
        # 'https://github.com/OCA/account-analytic',
        # 'https://github.com/OCA/server-ux oca-server-ux',
        # 'https://github.com/OCA/website oca-website',
        # 'https://github.com/OCA/ddmrp oca-ddmrp',
        # 'https://github.com/OCA/account-fiscal-rule oca-account-fiscal-rule',
        # 'https://github.com/OCA/storage oca-storage',
        # 'https://github.com/OCA/stock-logistics-reporting oca-stock-logistics-reporting',
        # 'https://github.com/OCA/geospatial oca-geospatial',
        # 'https://github.com/OCA/vertical-hotel oca-vertical-hotel',
        # 'https://github.com/OCA/server-auth oca-server-auth',
        # 'https://github.com/OCA/account-reconcile oca-account-reconcile',
        # 'https://github.com/OCA/server-backend oca-server-backend',
        # 'https://github.com/OCA/vertical-association oca-vertical-association',
        # 'https://github.com/OCA/account-invoicing oca-account-invoicing',
        # 'https://github.com/OCA/product-variant oca-product-variant',
        # 'https://github.com/OCA/queue oca-queue',
        # 'https://github.com/OCA/account-closing oca-account-closing',
        # 'https://github.com/OCA/iot oca-iot',
        # 'https://github.com/OCA/dms oca-dms',
        # 'https://github.com/OCA/margin-analysis oca-margin-analysis',
        # 'https://github.com/OCA/payroll oca-payroll',
        # 'https://github.com/OCA/hr-holidays oca-hr-holidays',
        # 'https://github.com/OCA/role-policy oca-role-policy',
        # 'https://github.com/OCA/apps-store oca-apps-store',
        # 'https://github.com/OCA/rest-framework rest-framework',
        # 'https://github.com/OCA/brand rest-brand',
        # 'https://github.com/OCA/report-print-send oca-report-print-send',
        # 'https://github.com/OCA/server-brand oca-server-brand',
        # 'https://github.com/OCA/oca-custom oca-oca-custom',
        # 'https://github.com/OCA/business-requirement oca-business-requirement',
        # 'https://github.com/OCA/commission oca-commission',
        # 'https://github.com/OCA/product-pack oca-product-pack',
        # 'https://github.com/OCA/currency oca-currency',
        # 'https://github.com/OCA/credit-control oca-credit-control',
        # 'https://github.com/OCA/stock-logistics-barcode oca-stock-logistics-barcode',
        # 'https://github.com/OCA/event oca-event',
        # 'https://github.com/OCA/hr-attendance oca-hr-attendance',
        # 'https://github.com/OCA/website-cms oca-website-cms',
        # 'https://github.com/OCA/survey oca-survey',
        # 'https://github.com/OCA/stock-logistics-transport oca-stock-logistics-transport',
        # 'https://github.com/OCA/manufacture-reporting oca-manufacture-reporting',
        # 'https://github.com/OCA/management-system oca-management-system',
        # 'https://github.com/OCA/fleet oca-fleet',
        # 'https://github.com/OCA/project-reporting oca-project-reporting',
        # 'https://github.com/OCA/stock-logistics-reporting oca-stock-logistics-reporting',
        # 'https://github.com/OCA/l10n-spain oca-l10n-spain',

        # # quilsoft-org
        # 'https://github.com/quilsoft-org/product quilsoft-org-product',
        'https://github.com/quilsoft-org/odoo-argentina quilsoft-org-odoo-argentina',
        # 'https://github.com/quilsoft-org/miscellaneous quilsoft-org-miscellaneous',
        # 'https://github.com/quilsoft-org/sale quilsoft-org-sale',
        # 'https://github.com/quilsoft-org/purchase quilsoft-org-purchase',
        'https://github.com/quilsoft-org/account-financial-tools quilsoft-org-account-financial-tools',
        # 'https://github.com/quilsoft-org/website quilsoft-org-website',
        'https://github.com/quilsoft-org/account-invoicing quilsoft-org-account-invoicing',
        # 'https://github.com/quilsoft-org/aeroo_reports quilsoft-org-aeroo_reports',
        # 'https://github.com/quilsoft-org/odoo-public-administration quilsoft-org-odoo-public-administration',
        'https://github.com/quilsoft-org/account-payment quilsoft-org-account-payment',
        # 'https://github.com/quilsoft-org/multi-company quilsoft-org-multi-company',
        # 'https://github.com/quilsoft-org/argentina-sale quilsoft-org-argentina-sale',
        # 'https://github.com/quilsoft-org/stock quilsoft-org-stock',
        # 'https://github.com/quilsoft-org/argentina-reporting quilsoft-org-argentina-reporting',
        # 'https://github.com/quilsoft-org/partner quilsoft-org-partner',
        # 'https://github.com/quilsoft-org/reporting-engine quilsoft-org-reporting-engine',
        'https://github.com/quilsoft-org/odoo-argentina-ee quilsoft-org-odoo-argentina-ee',
        'https://github.com/quilsoft-org/odoo-argentina-ce quilsoft-org-odoo-argentina-ce',
        # 'https://github.com/quilsoft-org/manufacture quilsoft-org-manufacture',
        # 'https://github.com/quilsoft-org/multi-store quilsoft-org-multi-store',
        # 'https://github.com/quilsoft-org/hr quilsoft-org-hr',
        # 'https://github.com/quilsoft-org/odoo-legal quilsoft-org-odoo-legal',
        # 'https://github.com/quilsoft-org/account-analytic quilsoft-org-account-analytic',
        # 'https://github.com/quilsoft-org/project quilsoft-org-project',

        # # Odoomates
        # 'https://github.com/odoomates/odooapps odoomates-odooapps',

		# OpenWorx			# ===========================================================================
		# 'https://github.com/Openworx/backend_theme ow-backend_theme',
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo jobiols/odoo-ent:15.0e',
        'postgres postgres:10.1-alpine',
    ]
}
