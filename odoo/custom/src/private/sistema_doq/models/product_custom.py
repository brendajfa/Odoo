from odoo import fields, models


class ProductCustom(models.Model):
    _name = 'product.custom'
    _description = 'Product Custom'

    name = fields.Char()

    # category_id = fields.Many2one(comodel_name='product.custom.category')
    category_ids = fields.Many2Many(comodel_name='product.custom.category')
    code = fields.Char(related = 'category_id.code')
    line_ids = fields.One2many(comodel_name='product.custom.lines', inverse_name='product_id')
    


class ProductCustomCategory(models.Model):
    _name = 'product.custom.category'
    _description = 'Product Custom Category'

    name = fields.Char()
    code = fields.Char()

class ProductCustomLines(models.Model):
    _name = 'product.custom.lines'
    _description = 'Product Custom Lines'

    quantity = fields.Integer()
    price = fields.Float()
    product_id = fields.Many2one(comodel_name='product.custom')
    