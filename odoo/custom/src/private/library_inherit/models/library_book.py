from odoo import  fields, models


class LibraryBook(models.Model):
    _inherit = 'library.book'

    purchase_date = fields.Date('Fecha de la compra')
    pages = fields.Integer('Número de págines')


