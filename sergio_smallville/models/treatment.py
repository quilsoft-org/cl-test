# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Treatment(models.Model):
    _name = "treatment"
    _description = 'Info treatment'

    code = fields.Text()
    name = fields.Text()
    doctor = fields.Text()

    def no_number(self):
        """validate is number"""
        for data in self:
            if '026' in data.code:
                return False
            else:
                return True
        return {}

    _constraints = [
        (no_number, 'Error: Invalid code', ['code']), 
    ]    