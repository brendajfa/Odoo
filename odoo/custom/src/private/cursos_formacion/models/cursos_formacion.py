from odoo  import fields, models

class CursosFormacion(models.Model):
    _name = 'cursos.formacion'
    _description = 'Modelo para reg'

    name = fields.Char()
    price = fields.Float()
    date = fields.Date(string="Date Purchase")
    course_type = fields.Selection(selection=[
        ('normal', 'Normal'),
        ('online', 'Online')
    ], string='Type')
    
    adress = fields.Char()