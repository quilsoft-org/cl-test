# For copyright and license notices, see __manifest__.py file in module root

from odoo.models import AbstractModel
from odoo import api
from datetime import datetime, timedelta


class PublisherWarrantyContract(AbstractModel):
    _inherit = "publisher_warranty.contract"

    @api.model
    def _get_sys_logs(self):
        _ = datetime.now() + timedelta(days=35)
        expiration_date = _.strftime('%Y-%m-%d %H:%M:%S')

        ret = {
            'messages': [],
            'enterprise_info': {
                'expiration_date': expiration_date,
                'expiration_reason': 'trial'
            }
        }
        return ret
