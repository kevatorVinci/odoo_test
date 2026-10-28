from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ReadingProgress(models.Model):
    _name = "my_library.reading.progress"
    _description = "Relevé de lecture"
    _order = "recorded_at desc"
    _rec_name = "display_name_progress"

    book_id = fields.Many2one(
        comodel_name="my_library.livre",
        string="Livre",
        required=True,
        ondelete="cascade",
    )
    page_number = fields.Integer(
        string="Page atteinte",
        required=True,
    )
    recorded_at = fields.Datetime(
        string="Date et heure",
        required=True,
        default=fields.Datetime.now,
    )
    display_name_progress = fields.Char(
        string="Libellé",
        compute="_compute_display_name_progress",
    )

    @api.depends("book_id.name", "page_number", "recorded_at")
    def _compute_display_name_progress(self):
        for progress in self:
            progress.display_name_progress = (
                f"{progress.book_id.name} - page {progress.page_number}"
            )

    @api.constrains("page_number", "book_id")
    def _check_page_number(self):
        for progress in self:
            book = progress.book_id
            if not book.page_count:
                raise ValidationError("Renseignez d'abord le nombre de pages du livre.")
            if progress.page_number <= 0:
                raise ValidationError("La page doit être un nombre positif.")
            if progress.page_number > book.page_count:
                raise ValidationError(
                    f"Le livre ne compte que {book.page_count} pages."
                )
