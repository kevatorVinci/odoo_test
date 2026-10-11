from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Livre(models.Model):
    _name = "my_library.livre"
    _description = "Livre"

    name = fields.Char(
        string="Titre",
        required=True,
    )

    author = fields.Char(
        string="Auteur",
        required=True,
    )

    publication_date = fields.Date(
        string="Date de publication",
    )

    isbn = fields.Char(
        string="ISBN",
        required=True,
    )

    description = fields.Text(
        string="Description",
    )

    price = fields.Float(
        string="Prix de vente",
        digits=(12, 2),
        default=0.0,
    )

    stock_quantity = fields.Integer(
        string="Quantité en stock",
        default=0,
    )

    active = fields.Boolean(
        string="En vente",
        default=True,
    )

    language = fields.Selection(
        selection=[
            ("fr", "Français"),
            ("en", "Anglais"),
            ("nl", "Néerlandais"),
        ],
        string="Langue",
        default="fr",
    )

    category_id = fields.Many2one(
        comodel_name="my.library.categorie",
        string="Category",
        ondelete="set null",
    )
    
    @api.constrains("isbn")
    def _check_isbn(self):
        for livre in self:
            if livre.isbn and len(livre.isbn) != 13:
                raise ValidationError("L'ISBN doit contenir 13 caractères.")

    _sql_constraints = [
        (
            "isbn_unique",
            "unique(isbn)",
            "Cet ISBN est déjà utilisé par un autre livre.",
        ),
    ]

    def action_put_on_sale(self):
        for livre in self:
            livre.active = True

    def action_remove_from_sale(self):
        for livre in self:
            livre.active = False
