from odoo import  fields, models


class BookAuthor(models.Model):
    _name = 'book.author'
    _description = 'Book Author'

    name = fields.Char()

    books_ids = fields.One2many(comodel_name='library.book', inverse_name='author_id')