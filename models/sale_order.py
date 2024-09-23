# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def _prepare_invoice(self):
        res = super()._prepare_invoice()

        res.update(
            {
                'invoice_date': fields.Date.context_today(self),
            }
        )

        return res

    def create_invoices_custom(self):
        for sale in self:
            sale._create_invoices(final=True)
