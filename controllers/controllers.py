# -*- coding: utf-8 -*-
from odoo import http

# class CjHrAttendance(http.Controller):
#     @http.route('/afnan_report/afnan_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/afnan_report/afnan_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('afnan_report.listing', {
#             'root': '/afnan_report/afnan_report',
#             'objects': http.request.env['afnan_report.afnan_report'].search([]),
#         })

#     @http.route('/afnan_report/afnan_report/objects/<model("afnan_report.afnan_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('afnan_report.object', {
#             'object': obj
#         })