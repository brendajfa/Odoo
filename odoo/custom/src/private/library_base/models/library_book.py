from odoo import  fields, models


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'library description'

    name = fields.Char(string='Nombre Libro')
    price = fields.Float('Precio')
    edition= fields.Integer('Edición')
    format = fields.Selection([
        ('fisic', 'Físico'),
        ('digital', 'Digital')
    ], string='Físico o Digital')
    web = fields.Char('Enlace web de compra')
    purchase = fields.Boolean('Se ha comprado')
    purchase_date = fields.Datetime('Fecha de la compra')

