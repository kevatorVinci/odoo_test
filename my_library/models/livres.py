from odoo import models, fields

class Livre (models.Model):
    _name = 'my_library.livre'
    _description = 'Livre'

    name = fields.Char(string='Titre', required=True)
    author = fields.Char(string='Auteur', required=True)
    publication_date = fields.Date(string='Date de publication')
    isbn = fields.Char(string='ISBN')
    description = fields.Text(string='Description')
