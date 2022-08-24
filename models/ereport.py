# -*- coding: utf8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError



class EReport(models.Model):
    _name = "hospital.ereport"
    _description = "E-Report"
    _rec_name = 'rapor_no'

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
    ], string="Rapor Onay Durumu", default='1')

    rapor_olusturan_doktor = fields.Many2one('hospital.doctor', string="Raporu Oluşturan Doktor")
    doctor_name = fields.Char(string="Doktor Adı", related="rapor_olusturan_doktor.name")
    doctor_surname = fields.Char(string="Doktor Soyadı", related="rapor_olusturan_doktor.surname")

    rapor_teshis_listesi = fields.One2many('ereport.teshis.line', 'ereport_id', string="E-Rapor Teşhis Listesi")
    rapor_doktor_listesi = fields.Many2many('hospital.doctor', string="E-Rapor Doktor Listesi")
    rapor_doktor_listesi2 = fields.One2many('ereport.doctor.line', 'ereport_id', string="E-Rapor Doktor Listesi")
    rapor_etkin_madde_listesi = fields.Many2many('hospital.etkin_madde', string="E-Rapor Etkin Madde Listesi")
    rapor_aciklama_listesi = fields.One2many('hospital.ereport.explanation', 'ereport_id', string="E-Rapor Açıklama Listesi")
    rapor_tani_listesi = fields.Many2many('hospital.ereport.tani', string="E-Rapor Tanı Listesi")
    rapor_ilave_deger_listesi2 = fields.One2many('hospital.ereport.ilave_deger', 'ereport_id', string="E-Rapor İlave Değer Listesi")

    state = fields.Selection([
        ('taslak', 'Taslak'),
        ('heyet_onayinda', 'Heyet Onayında'),
        ('bashekim_onayinda', 'Başhekim Onayında'),
        ('onaylanmadi', 'Onaylanmadı'),
        ('onaylandi', 'Onaylandı'),
        ('silindi', 'E-Rapor Silindi'),
    ], default="taslak", string="Durum")



    def send_to_confirmation(self):
        ereport = self.env['hospital.ereport'].search([('rapor_no', '=', self.rapor_no)])

        ereport.state = 'heyet_onayinda'


class EreportDoctorLine(models.Model):
    _name = "ereport.doctor.line"

    ereport_id = fields.Many2one('hospital.ereport', string="E-Report")
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    name = fields.Char(string="Doctor name", related="doctor_id.name")
    surname = fields.Char(string="Doctor surname", related="doctor_id.surname")
    doctor_tc = fields.Char(string="Doctor Tc", related="doctor_id.doctor_tc")


# EraporTeshisDVO
class EreportTeshisLine(models.Model):

    _name = "ereport.teshis.line"

    ereport_id = fields.Integer()
    rapor_teshis_kodu = fields.Many2one('hospital.ereport.teshis', string="Teşhis Kodu")
    baslangic_tarihi = fields.Date(string="Başlangıç Tarihi", date_format="dd.MM.yyyy")
    bitis_tarihi = fields.Date(string="Bitiş Tarihi", date_format="dd.MM.yyyy")
    tani_listesi = fields.Many2many('hospital.ereport.tani')
