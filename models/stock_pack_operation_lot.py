# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class StockPackOperationLot(models.Model):
    _inherit = 'stock.pack.operation.lot'

    @api.onchange('lot_name')
    def _onchange_lot_name(self):
        if self.lot_name:
            parts = self.lot_name.split("'")
            if len(parts) > 1:
                self.lot_name = parts[0]
                self.qty = parts[1]
