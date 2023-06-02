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

    author_id = fields.Many2one(comodel_name='books.author')
    genre_ids = fields.Many2many(comodel_name='books.genre', string='Genres')
    


    
class BookAuthor(models.Model):
    _name = 'books.author'
    _description = 'Book Author'

    name = fields.Char()

    book_ids = fields.One2many(comodel_name='library.book', inverse_name='author_id')


class BookgGenre(models.Model):
    _name = 'books.genre'
    _description = 'Book Genre'

    name = fields.Char()

#         raise exception.with_traceback(None) from new_cause
# psycopg2.errors.UndefinedTable: relation "books_genre_library_book_rel" does not exist
# LINE 1: ... books_genre_library_book_rel.books_genre_id FROM books_genr...