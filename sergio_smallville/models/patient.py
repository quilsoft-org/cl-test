# -*- coding: utf-8 -*-
from odoo import models, fields, api
import re


class Patients(models.Model):
    _name = "patients"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Info patients'

    sequence = fields.Char(readonly="1")
    name = fields.Char()
    dni = fields.Char(track_visibility='onchange')
    treatment_ids = fields.Many2many('treatment')
    discharge_date = fields.Datetime()
    update_date = fields.Datetime()
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('high', 'Alta'),
        ('down', 'Baja')
        ], 'Status', default='draft', track_visibility='onchange')


    @api.model
    def _get_default_company(self):
        """get company"""
        return self.env.user.company_id

    company_id = fields.Many2one('res.company', string='Company', required=True, default=_get_default_company)

    @api.model
    def create(self, vals):
        rec = super(Patients, self).create(vals)
        if not rec.sequence:
            rec._create_check_sequence()
        return rec

    @api.one
    def _create_check_sequence(self):
        """ Create a check sequence"""
        SEQUENCE_CODE = 'patient.sequence'
        IrSequence = self.env['ir.sequence']
        if IrSequence.search([('code', '=', SEQUENCE_CODE)]):
            self.sequence = IrSequence.next_by_code(SEQUENCE_CODE)
        else:
            seq = IrSequence.sudo().create({
                'code': SEQUENCE_CODE,
                'name': "Patient Sequence",
                'implementation': 'no_gap',
                'prefix': 'PA',
                'padding': 6,
                'number_increment': 1,
                'number_next_actual': 1,
            })
            self.sequence = seq.next_by_code(SEQUENCE_CODE)

    def is_number(self):
        """validate is number"""
        for data in self:
            if data.dni.isdigit():
                return True
            else:
                return False
        return {}

    _constraints = [
        (is_number, 'Error: Invalid DNI, only number', ['dni']), 
    ]