# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class JobCostLine(models.Model):
    _inherit = 'job.cost.line'

    @api.depends('custom_mpr_line_ids', 'custom_mpr_line_ids.qty', 'custom_mpr_line_ids.requisition_id.state')
    def _compute_actual_requisition_quantity(self):
        for rec in self:
            rec.actual_requisition_qty = sum([p.requisition_id.state not in ['cancel'] and p.qty for p in rec.custom_mpr_line_ids])

    @api.depends('actual_requisition_qty','cost_price')
    def _compute_actual_requisition_cost(self):
        self.actual_requisition_cost = self.actual_requisition_qty * self.cost_price

    actual_requisition_qty = fields.Float(
        string='Cnt. Req. Picking',
        compute='_compute_actual_requisition_quantity',
        store=True,
        digits=(16, 6),
    )

    actual_requisition_cost = fields.Float(
        string='Cost. Req. Picking',
        compute='_compute_actual_requisition_cost',
        store=True,
        digits=(16, 6),
    )

    custom_mpr_line_ids = fields.One2many(
        'material.purchase.requisition.line',
        'custom_job_costing_line_id',
        string="Requisición de Materiales",
    )