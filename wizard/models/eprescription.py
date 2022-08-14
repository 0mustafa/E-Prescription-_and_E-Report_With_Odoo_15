# -*- coding: utf8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class EPrescriptionWizard(models.TransientModel):
    _name = "hospital.eprescription.wizard"
    _description = "E-Prescription Wizard"
    _rec_name = 'seri_no'

    doctor_id = fields.Many2one('hospital.doctor', string="Doktor", required=True)
    brans_kod = fields.Char(string="Branş Kod", related="doctor_id.brans_kod")

    patient_id = fields.Many2one('hospital.epatient', string="Patient", required=True)
    patient_name = fields.Char(string="Hasta Ad", related="patient_id.name")
    patient_surname = fields.Char(string="Hasta Soyad", related="patient_id.surname")

    recete_tur = fields.Selection([
        ('1', 'Normal'),
        ('2', 'Kırmızı'),
        ('3', 'Turuncu'),
        ('4', 'Mor'),
        ('5', 'Yeşil')
    ], string="Reçete Türü", required=True)
    recete_alt_tur = fields.Selection([
        ('1', 'Ayaktan Reçetesi'),
        ('2', 'Yatan Reçetesi'),
        ('3', 'Taburcu Reçetesi'),
        ('4', 'Günübirlik Reçetesi'),
        ('5', 'Acil Reçetesi'),
        ('6', 'Yeşil Alan Reçetesi'),
        ('7', 'Evde Bakım Reçetesi'),
        ('8', 'Gezici Sağlık Hizmeti Reçetesi')
    ], string="Reçete Alt Türü", required=True)

    tesis_kod = fields.Char(string="Tesis Kodu")
    takip_no = fields.Char(string="Takip No")
    provizyon_tip = fields.Selection([
        ('1', 'Normal'),
        ('2', 'Trafik'),
        ('3', 'Doğal Afet'),
        ('4', 'Adli Vaka'),
        ('5', 'İş Kazası'),
        ('6', 'Meslek Hastalığı'),
        ('7', 'Analık Hali'),
        ('8', '3713/21')
    ], string="Provizyon Tipi", required=True)
    protokol_no = fields.Char(string="Protokol No")
    seri_no = fields.Char(string="Seri No")

    erecete_no = fields.Char(string="E-Reçete No")
    erecete_aciklama_turu = fields.Integer(string="E-Reçete Açıklama Türü")
    erecete_aciklama = fields.Char(string="E-Reçete Açıklama")
    erecete_tani_kodu = fields.Char(string="E-Reçete Tanı Kodu")
    erecete_tani_adi = fields.Char(string="E-Reçete Tanı Adı")

    today = fields.Date(string='Tarih', default=fields.Date.context_today, date_format="dd.MM.yyyy")

    pharmacy_line_ids = fields.One2many('eprescription.pharmacy.lines', 'eprescription_id', string="Pharmacy Lines", required=True)
    explanation_line_ids = fields.One2many('eprescription.explanation.lines', 'eprescription_id',
                                           string="Explanation Lines", required=True)

    diagnosis_line_ids = fields.Many2many('hospital.diagnosis', string="Diagnosises", required=True)

    state = fields.Selection([
        ('taslak', 'Taslak'),
        ('gonderildi', 'Medulaya Gönderildi'),
        ('silindi', 'E-Reçete Silindi')
    ], default="taslak", string="Durum")
