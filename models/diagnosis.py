# -*- coding: utf8 -*-
import dateutil.utils

from odoo import models, fields, api


class Diagnosis(models.Model):

    _name = "hospital.diagnosis"
    _description = "Hospital Diagnosis"
    _rec_name = 'tani_kodu'

    tani_kodu = fields.Char(string="Tanı Kodu")
    tani_adi = fields.Char(string="Tanı Adı")
