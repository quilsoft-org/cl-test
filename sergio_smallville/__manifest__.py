# -*- coding: utf-8 -*-
{
    'name': "vertical_hospital",

    'author': "Sergio",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': [
        'base',
        'mail',
    ],
    'data': [
        #'data/groups.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/main_menu_view.xml',
        'views/patient_view.xml',
        'views/treatment_view.xml',
        'reports/patient_report.xml',
    ],
}