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

    # practica 2
    dealer_ids = fields.One2many(comodel_name='books.dealer',
                                 inverse_name='book_id')
    editorial_ids = fields.One2many(comodel_name='books.editorial',
                                    inverse_name='book_id')
    # genre_ids = fields.Many2many(related="author_id.genre_ids", string='Genres')

    # Modulo 5 practica 1
    genre_ids = fields.Many2many(comodel_name='books.genre', string='Genres')

    @api.onchange('author_id')
    def _onchange_author_id(self):
        self.genre_ids = self.author_id.genre_ids

    total_units = fields.Float(compute="_compute_total_units")  # Yo hubiese puesto fields.Integer
    total_sales = fields.Float(compute="_compute_total_sales")

    @api.depends('price', 'dealer_ids')
    def _compute_total_units(self):
        for rec in self:
            rec.total_units = 0
            for dealer in rec.dealer_ids:
                rec.total_units += dealer.sale_unit
            rec.total_sales = rec.total_units * rec.price

    full_name = fields.Char(compute="_compute_full_name", readonly=False,
                            store=True)

    @api.depends('author_id', 'name')
    def _compute_full_name(self):
        for rec in self:
            rec.full_name = rec.name + " - " + rec.author_id.name


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        res = super().onchange_partner_id
        if self.partner_id:
            self.client_order_ref = self.partner_id.vat
        return res


class BookDealer(models.Model):
    _name = 'books.dealer'
    _description = 'Book Dealer'

    price_unit = fields.Float(string='Price Unit')
    sale_unit = fields.Integer(string='Unit Sales')
    book_id = fields.Many2one(comodel_name='library.book', string='Book ID')
    dealer_id = fields.Many2one(comodel_name='res.partner', string='Dealer')  # WHAT? contacto
    # SOLUCION: dealer_id = fields.Many2one(comodel_name='res.partner', string = "Dealer")


class BookEditorial(models.Model):
    _name = 'books.editorial'
    _description = 'Book Editorial'

    page_number = fields.Integer(string='Number of Pages')
    book_id = fields.Many2one(comodel_name='library.book', string='Book ID')
    editorial_id = fields.Many2one(comodel_name='res.partner',
                                   string='Editorial')  # WHAT? contacto


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