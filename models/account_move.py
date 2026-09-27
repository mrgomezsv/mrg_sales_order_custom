# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        res = super().action_post()
        source_orders = self.line_ids.sale_line_ids.order_id
        for picking in getattr(source_orders, 'picking_ids', []):
            try:
                for move in picking.move_ids:
                    if hasattr(move, 'quantity'):
                        move.quantity = move.product_uom_qty
                    elif hasattr(move, 'quantity_done'):
                        move.quantity_done = move.product_uom_qty
                if hasattr(picking, 'button_validate'):
                    picking.button_validate()
            except Exception:
                pass
        return res
