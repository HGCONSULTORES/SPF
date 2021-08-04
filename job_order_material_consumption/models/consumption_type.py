# -*- coding: utf-8 -*-
# Part of GECOERP. Ltd. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class ConsumptionType(models.Model):
     _name = 'consumption.type'
     _description = 'Consumption Type'

     name = fields.Char(
        string='Name',
        required=True,
    )
     
