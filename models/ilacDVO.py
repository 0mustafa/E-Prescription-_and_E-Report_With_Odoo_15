# -*- coding: utf8 -*-
import dateutil.utils

from odoo import models, fields, api


class IlacDVO(models.Model):

    _name = "hospital.ilac"
    _description = "İlaç Tablosu"
    _rec_name = "barcode"

    barcode = fields.Char(string="İlaç Barkodu")
    ilac_adi = fields.Char(string="İlaç Adı")
    sgk_ilac_kodu = fields.Char(string="SGK İlaç Kodu")
    ambalaj_miktari = fields.Float(string="Ambalaj miktarı")
    tek_doz_miktari = fields.Float(string="Tek Doz Miktarı")
    kutu_birim_miktari = fields.Float(string="Kutu Birim Miktari")
    ayaktan_odenme_sarti = fields.Selection([
        ('1', 'Ödenir'),
        ('2', 'Raporla Ödenir'),
        ('3', 'Ödenmez')
    ], string="Ayaktan Ödenme Şartı")
    yatan_odenme_sarti = fields.Selection([
        ('1', 'Ödenir'),
        ('2', 'Raporla Ödenir'),
        ('3', 'Ödenmez')
    ], string="Yatan Ödenme Şartı")
    etkin_madde_kodu = fields.Char(string="Etkin Madde Kodu")

    def name_get(self):
        result = []
        for rec in self:
            name = rec.barcode + ' : ' + rec.ilac_adi
            result.append((rec.id, name))
        return result
