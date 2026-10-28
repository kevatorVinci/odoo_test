from odoo import fields, models


class ReadingProgressWizard(models.TransientModel):
    _name = "my_library.reading.progress.wizard"
    _description = "Enregistrer une progression de lecture"

    book_id = fields.Many2one(
        comodel_name="my_library.livre",
        string="Livre",
        required=True,
        readonly=True,
    )
    page_number = fields.Integer(
        string="Page atteinte",
        required=True,
    )

    def action_confirm(self):
        self.ensure_one()
        self.env["my_library.reading.progress"].create(
            {
                "book_id": self.book_id.id,
                "page_number": self.page_number,
            }
        )
        return {"type": "ir.actions.act_window_close"}