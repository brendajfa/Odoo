from odoo  import fields, models

class CursosNewModel(models.Model):
    _name = 'new.modelcursos'
    _description = 'New Model'

    name = fields.Char()
    product_code = fields.Integer(string='Product Code 2')