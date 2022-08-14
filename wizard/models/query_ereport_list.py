# -*- coding: utf8 -*-
import datetime

from odoo import models, fields, api


class QueryEreportListWizard(models.TransientModel):

    _name = "ereport.list.query.wizard"
    _description = "E-Rapor Listesi Wizard"

    patient_name = fields.Char(string="Hasta Adı")
    patient_surname = fields.Char(string="Hasta Soyadı")
    ereports_list = fields.Many2many('hospital.ereport', string="Hastaya ait e-raporlar")
