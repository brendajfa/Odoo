from odoo import api, fields, models


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'library description'

    name = fields.Char(string='Nombre Libro')
    price = fields.Float('Precio')
    edition = fields.Integer('Edición')
    format = fields.Selection([
        ('fisic', 'Físico'),
        ('digital', 'Digital')
    ], string='Físico o Digital')
    web = fields.Char('Web')
    purchase = fields.Boolean('Se ha comprado')
    purchase_date = fields.Datetime('Fecha de compra')

    # practica 1
    author_id = fields.Many2one(comodel_name='books.author',
                                string='Author ID')
    # genre_ids = fields.Many2many(comodel_name='books.genre', string='Genres')

    # practica 2
    dealer_ids = fields.One2many(comodel_name='books.dealer',
                                 inverse_name='book_id')
    editorial_ids = fields.One2many(comodel_name='books.editorial',
                                    inverse_name='book_id')
    genre_ids = fields.Many2many(related="author_id.genre_ids", string='Genres')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_type = fields.Char(string='Tipo de venta')

    @api.onchange('')
    def _onchange_(self):
        pass   
    

class BookDealer(models.Model):
    _name = 'books.dealer'
    _description = 'Book Dealer'

    price_unit = fields.Float(string='Price Unit')
    sale_unit = fields.Integer(string='Unit Sales')

    book_id = fields.Many2one(comodel_name='library.book',
                              string='Book ID')

    dealer_id = fields.Many2one(comodel_name='res.partner', string='Dealer') # WHAT? contacto
    # SOLUCION: dealer_id = fields.Many2one(comodel_name='res.partner', string="Dealer")


class BookEditorial(models.Model):
    _name = 'books.editorial'
    _description = 'Book Editorial'

    page_number = fields.Integer(string='Number of Pages')

    book_id = fields.Many2one(comodel_name='library.book', string='Book ID')

    editorial_id = fields.Many2one(comodel_name='res.partner', string='Editorial') # WHAT? contacto


class BookAuthor(models.Model):
    _name = 'books.author'
    _description = 'Book Author'

    name = fields.Char()

    book_ids = fields.One2many(comodel_name='library.book',
                               inverse_name='author_id')
    genre_ids = fields.Many2many(comodel_name='books.genre', string='Genres')


class BookgGenre(models.Model):
    _name = 'books.genre'
    _description = 'Book Genre'

    name = fields.Char()

#         raise exception.with_traceback(None) from new_cause
# psycopg2.errors.UndefinedTable: relation "books_genre_library_book_rel" does not exist
# LINE 1: ... books_genre_library_book_rel.books_genre_id FROM books_genr...