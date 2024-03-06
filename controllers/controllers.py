# -*- coding: utf-8 -*-
# from odoo import http


# class MslPaymentReceipt(http.Controller):
#     @http.route('/msl_payment_receipt/msl_payment_receipt', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/msl_payment_receipt/msl_payment_receipt/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('msl_payment_receipt.listing', {
#             'root': '/msl_payment_receipt/msl_payment_receipt',
#             'objects': http.request.env['msl_payment_receipt.msl_payment_receipt'].search([]),
#         })

#     @http.route('/msl_payment_receipt/msl_payment_receipt/objects/<model("msl_payment_receipt.msl_payment_receipt"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('msl_payment_receipt.object', {
#             'object': obj
#         })
