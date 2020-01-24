# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class StockMoveLots(models.Model):
    _inherit = 'stock.move.lots'

    @api.onchange('lot_id')
    def _onchange_lot_id(self):
        if self.lot_id:
            parts = self.lot_id.name.split("'")
            if len(parts) > 1:
                # parent_id = self.env.context.get('parent') TODO
                self.lot_id = self.env['stock.production.lot'].search([
                    # ('product_id', '=', parent_id.product_id),
                    ('name', '=', parts[0]),
                ], limit=1)
                self.quantity = parts[1]
                self.quantity_done = parts[1]
