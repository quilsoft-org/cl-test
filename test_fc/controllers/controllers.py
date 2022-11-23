# -*- coding: utf-8 -*-
from odoo import http

class MyModule(http.Controller):
    # @http.route('/productos/<model("product.template"):product>/', auth='public')
    # def fun_product(self, product):
    #     return http.request.render('custom.product', {
    #     	"product": product
    #     	})

#     @http.route('/my_module/my_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_module.listing', {
#             'root': '/my_module/my_module',
#             'objects': http.request.env['my_module.my_module'].search([]),
#         })

    @http.route('/partners/id/<model("res.partner"):partner>/', auth='public', website=False, csrf=False, type='json', methods=['GET','POST'])
    def object(self, partner, **kw):
        # import pdb;pdb.set_trace()
        # return '{"id": '+str(partner.id)+',"name": "'+partner.name+'","street": "'+partner.name+'","email": "'+partner.email+'"}'
        
        contacto = []
        contacto.append({
	    	'id': partner.id,
	    	'name': partner.name,
	    	'street': partner.street,
	    	'email': partner.email,
	    	})
        return contacto
 