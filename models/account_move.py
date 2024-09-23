# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        res = super().action_post()
        source_orders = self.line_ids.sale_line_ids.order_id
        for picking in source_orders.picking_ids:
            picking.quantity_done = picking.product_uom_qty
            picking.button_validate
