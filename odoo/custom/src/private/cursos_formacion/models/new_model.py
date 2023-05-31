from odoo import api, fields, models


class NewModel(models.Model):
    _name = 'new.model'
    _description = 'New Description'

    name = fields.Char()
    product_code = fields.Integer(string='Product Code 2')

