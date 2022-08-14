# -*- coding: utf8 -*-

from odoo import models, fields, api


class TeshisWizard(models.TransientModel):
    _name = "hospital.teshis.wizard"
    _description = "Teşhis Wizard"

    teshis_ids = fields.Many2many('hospital.ereport.teshis', string="Teşhis Listesi")
