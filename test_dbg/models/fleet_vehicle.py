from odoo import _, api, Command, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    def write(self, vals):

        import wdb;
        wdb.set_trace()

        res = super().write(vals)
