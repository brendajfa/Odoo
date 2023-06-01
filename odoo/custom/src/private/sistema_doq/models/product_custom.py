from odoo import fields, models


class ProdctCustom(models.Model):
    _name = 'product.custom'
    _description = 'Product Custom'

    name = fields.Char()

    category_id = fields.Many2one(comodel_name='product.custom.category')
    


class ProdctCustomCategory(models.Model):
    _name = 'product.custom.category'
    _description = 'Product Custom Category'

    name = fields.Char()
    code = fields.Char()
