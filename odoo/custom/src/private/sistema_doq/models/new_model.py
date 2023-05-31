from odoo  import fields, models

class NewModel(models.Model):
    _name = 'newer.model'
    _description = 'New Model Description'

    name = fields.Char(
        translate=True
    )
    product_code = fields.Integer(string='Product Code 2')