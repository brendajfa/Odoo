from odoo import fields, models, api


class ModuleAuth(models.Model):
    _name = 'books.author'
    _description = 'autores'

    name = fields.Char(required=True)
    books_ids = fields.One2many(
        comodel_name='books.book', inverse_name='author_id')
    genre_ids = fields.Many2many(comodel_name='books.genre', string="Genres")

    # Yo como usuario [quiero 
    # que al eliminar un autor se 
    # eliminen todos lo libros asociados
    @api.model
    def unlink(self):
        for rec in self:
            rec.books_ids.unlink()
        return super().unlink()

    def write(self, values):
        # Con [(6,0,[ids])] podemos escribir en un 
        # campo relacionado one2many o many2many
        res = super().write(values)
        self.books_ids.write({
            'genre_ids': [(6, 0, self.genre_ids.ids)]
        })
        return res
