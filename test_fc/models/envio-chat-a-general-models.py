# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

# class my_module(models.Model):
#     _name = 'my_module.my_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class ResPartner(models.Model):
    _inherit = "res.partner"
    es_frecuente = fields.Boolean(string='Es Frecuente', required=True)
    puntuacion = fields.Integer(string='Puntuacion', required=True, track_visibility='onchange')

class VerificarCantidadPresupuestos(models.Model):
   _name = 'verificar.presupuestos'
   def verificar_cantidad(self):
       orders = self.env['sale.order'].search([('state','=','draft')])
       contador = 0
       for order in orders:
           if order.date_order.strftime('%Y-%m-%d') == datetime.today().strftime('%Y-%m-%d'):
               contador = contador + 1
       # if contador > 0:
           # import pdb;pdb.set_trace()
           # notification_ids = [((0, 0, {
           # 'res_partner_id': user.partner_id.id,
           # 'notification_type': 'inbox'}))]
       channels = self.env['mail.channel'].search([('id','=',1)])
       user_id = self.env.user.id # odooBoot
       message = ("Hay más de 5 presupuestos!") 
       channels[0].message_post(author_id=user_id,
                   body=(message),
                   message_type='notification',
                   subtype_xmlid="mail.mt_comment",
                   notify_by_email=False,
                   )     
       # import pdb;pdb.set_trace()
       