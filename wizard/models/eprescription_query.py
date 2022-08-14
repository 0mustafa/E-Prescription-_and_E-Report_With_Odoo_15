# -*- coding: utf8 -*-

from odoo import models, fields, api


class EPrescriptions(models.TransientModel):
    _name = "hospital.eprescription.query.wizard"
    _description = "E-Prescription wizard"

    doctor_id = fields.Many2one('hospital.doctor', string="Doktor", required=True)
    brans_kod = fields.Char(string="Branş Kod", related="doctor_id.brans_kod")

    patient_id = fields.Many2one('hospital.epatient', string="Patient", required=True)
    patient_name = fields.Char(string="Hasta Ad", related="patient_id.name")
    patient_surname = fields.Char(string="Hasta Soyad", related="patient_id.surname")

    recete_tur = fields.Integer(string="Reçete Türü", required=True)
    recete_alt_tur = fields.Integer(string="Reçete Alt Türü", required=True)

    tesis_kod = fields.Char(string="Tesis Kodu")
    takip_no = fields.Char(string="Takip No")
    provizyon_tip = fields.Integer(string="Provizyon Tipi")
    protokol_no = fields.Char(string="Protokol No")
    seri_no = fields.Char(string="Seri No")

    erecete_no = fields.Char(string="E-Reçete No")
    erecete_aciklama_turu = fields.Integer(string="E-Reçete Açıklama Türü")
    erecete_aciklama = fields.Char(string="E-Reçete Açıklama")
    erecete_tani_kodu = fields.Char(string="E-Reçete Tanı Kodu")
    erecete_tani_adi = fields.Char(string="E-Reçete Tanı Adı")

    today = fields.Date(string='Tarih', default=fields.Date.context_today, date_format="dd.MM.yyyy")


# İlaç ekle
class AppointmentPharmacyLines(models.TransientModel):
    _name = "eprescription.pharmacy.lines.wizard"
    _description = "E-Prescription Pharmacy Lines"

    kullanim_sekli = fields.Integer(string="Kullanım Şekli")
    kullanim_doz1 = fields.Integer(string="Kullanım Doz 1")
    kullanim_doz2 = fields.Float(string="Kullanım Doz 2")
    kullanim_periyot = fields.Integer(string="Kullanım Periyodu")
    kullanim_periyot_birimi = fields.Selection([
        ('3', 'Günde'),
        ('4', 'Haftada'),
        ('5', 'Ayda'),
        ('6', 'Yılda')
    ], string="Kullanım Periyot Birimi")
    quantity = fields.Integer(string="Adet", default=1)

    erecete_ilac_aciklama_turu = fields.Selection([
        ('1', 'Teşhis/Tanı'),
        ('2', 'Tedavi Süresi'),
        ('3', 'Hasta Güvenlik ve İzleme Formu'),
        ('4', 'Tetkik Sonucu'),
        ('5', 'Endikasyon Dışı Kullanım İzni'),
        ('99', 'Diğer')
    ], string="E-Reçete İlaç Açıklama Türü")
    erecete_ilac_aciklama = fields.Text(string="E-Reçete İlaç Açıklama")

    eprescription_id = fields.Many2one('hospital.eprescription')
    # sub_total = fields.Float(string="Total", compute="_compute_sub_total")


# E-Reçete Açıklama Ekle
class EprescriptionsExplanationLines(models.TransientModel):
    _name = "eprescription.explanation.lines.wizard"
    _description = "E-Prescription Explanation Lines"

    explanation_id = fields.Many2one('hospital.explanation')
    eprescription_id = fields.Many2one('hospital.eprescription')
    aciklama_turu = fields.Selection([
        ('1', 'Teşhis/Tanı'),
        ('2', 'Tedavi Süresi'),
        ('3', 'Hasta Güvenlik ve İzleme Formu'),
        ('4', 'Tetkik Sonucu'),
        ('5', 'Endikasyon Dışı Kullanım İzni'),
        ('99', 'Diğer')
    ], string="Açıklama Türü")
    aciklama = fields.Text(string="E-Reçete Açıklaması")

