# For copyright and license notices, see __manifest__.py file in module root
from . import models
from odoo import api, SUPERUSER_ID

def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['publisher_warranty.contract'].update_notification()
