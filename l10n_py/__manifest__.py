# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Paraguayan - Accounting',
    'version': '13.0.0.0.0',
    'category': 'Localization',
    'description': """
Paraguayan accounting chart in Odoo.
====================================

Install paraguayan chart of accounts.
    """,
    'depends': [
        'account',
    ],
    'data': [
        'data/l10n_py.xml',
        'data/account.account.template.csv',
        'data/l10n_py_post.xml',
    ],
    'demo': [
        'demo/account_bank_statement_demo.xml',
        'demo/account_invoice_demo.xml',
        'demo/account_reconcile_model.xml',
    ],
    'uninstall_hook': 'uninstall_hook',
}
