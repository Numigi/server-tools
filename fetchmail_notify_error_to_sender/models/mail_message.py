# Copyright 2019 Eficent <http://www.eficent.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class MailMessage(models.Model):
    _inherit = 'mail.message'

    @api.multi
    def _invalidate_documents(self):
        """WAITING the merge of https://github.com/odoo/odoo/pull/31799"""
        super(MailMessage,
              self.filtered(lambda r: r.model != 'fetchmail.server')
              )._invalidate_documents()
