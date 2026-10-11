from odoo import models, fields


class Categorie(models.Model):
    _name = "my.library.categorie"
    _description = "Book Category"

    name = fields.Char(
        string="Name",
        required=True,
    )
