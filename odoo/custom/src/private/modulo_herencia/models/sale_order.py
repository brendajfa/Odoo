from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    reservation = fields.Boolean()
    date_order = fields.Date()
    
