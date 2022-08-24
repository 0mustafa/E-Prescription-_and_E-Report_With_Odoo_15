# -*- coding: utf8 -*-

from odoo import models, fields, api


class EReportWizard(models.TransientModel):
    _name = "hospital.ereport.wizard"
    _description = "E-Report Wizard"

    tesis_kod = fields.Char(string="Tesis Kodu", required=True)
    rapor_takip_no = fields.Char(string="Rapor Takip No")   # MEDULA uretecek
    protokol_no = fields.Char(string="Protokol No", required=True)  # Sağlık tesisi uretecek
    takip_no = fields.Char(string="Takip No")  # MEDULA takip numarası

    patient_id = fields.Many2one('hospital.epatient', string="Hasta")
    patient_name = fields.Char(string="Hasta Adı", related="patient_id.name")
    patient_surname = fields.Char(string="Hasta Soyadı", related="patient_id.surname")

    rapor_no = fields.Char(string="Rapor No", required=True)   # Sağlık tesisi uretecek
    rapor_tarihi = fields.Date(string="Rapor Tarihi", default=fields.Date.context_today, date_format="dd.MM.yyyy")
    rapor_duzenleme_turu = fields.Selection([
        ('1', 'Sağlık Kurulu Raporu'),
        ('2', 'Uzman Hekim Raporu')
    ], string="Rapor Düzenleme Türü", required=True)
    rapor_onay_durumu = fields.Selection([
        ('1', 'Onay Bekliyor'),
        ('2', 'Onaylandı')
    ], string="Rapor Onay Durumu", required=True)

    rapor_olusturan_doktor = fields.Many2one('hospital.doctor', string="Raporu Oluşturan Doktor")

    rapor_teshis_listesi = fields.One2many('ereport.teshis.line', 'ereport_id', string="E-Rapor Teşhis Listesi")
    rapor_doktor_listesi = fields.Many2many('hospital.doctor', string="E-Rapor Doktor Listesi")
    rapor_etkin_madde_listesi = fields.Many2many('hospital.etkin_madde', string="E-Rapor Etkin Madde Listesi")
    rapor_aciklama_listesi = fields.One2many('hospital.ereport.explanation', 'ereport_id', string="E-Rapor Açıklama Listesi")
    rapor_tani_listesi = fields.Many2many('hospital.diagnosis', string="E-Rapor Tanı Listesi")
    rapor_ilave_deger_listesi2 = fields.One2many('hospital.ereport.ilave_deger', 'ereport_id', string="E-Rapor İlave Değer Listesi")





