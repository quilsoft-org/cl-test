# -*- coding: utf-8 -*-
{
    'name': "test_fc",

    'summary': """
        Test Franco Corvalan""",

    'description': """
        Test Franco Corvalan
    """,

    'author': "Test Franco Corvalan",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'demo/demo.xml',
	'reports/contacts_report.xml',
        'reports/contacts_report_view.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}