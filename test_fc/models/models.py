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
       if contador > 0:
           # ----------ENVIO DE MENSAJE A CANAL "GENERAL"-----------------------------------
           # import pdb;pdb.set_trace()
           # notification_ids = [((0, 0, {
           # 'res_partner_id': user.partner_id.id,
           # 'notification_type': 'inbox'}))]
             channels = self.env['mail.channel'].search([('id','=',1)])
             user_id = self.env.user.partner_id.id
             message = ("Hay más de 5 presupuestos!") 
             channels[0].message_post(author_id=user_id,
                   body=(message),
                   message_type='notification',
                   subtype_xmlid="mail.mt_comment",
                   notify_by_email=False,
                   )
           # ----------INCREMENTO EN 1 DE PARAMETRO "quotation.no"--------------------------
             quotation = self.env['ir.config_parameter'].search([('key','=','quotation.no')])
             quotation_value = int(quotation.value) + 1
             quotation.write({'value': quotation_value})

class Lagartijas(models.Model):
   _name = 'lagartijas'
   apodo = fields.Char(string='Apodo')
   peso = fields.Integer(string='Peso')
   color = fields.Char(string='Color')
   alta = fields.Datetime(string='Alta')

# class ResConfigSettings(models.TransientModel):
#     _inherit = "res.config.settings"
#     numero_presupuestos = fields.Integer(string='Nro de presupuestos')

   # actualizacion = fields.Datetime(string='Actualizacion') # 1) write_date , 2) __last_update
   # usuario_alta = fields.Many2one('res.users', required=True) # create_uid
   # usuario_actualizacion = fields.Many2one('res.users', required=True) # write_uid
   # import pdb;pdb.set_trace()
       