# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError

import base64

class sale_order(models.Model):
    _inherit = 'sale.order'

    purchase_no = fields.Char(string="رقم الشراء")
    external_no = fields.Char(string="الرقم الخارجي")
    transaction_no = fields.Char(string="رمز معاملة الفاتورة")
    invoice_issue_date = fields.Datetime(string="تاريخ اصدار الفاتورة")
    date_of_supply = fields.Datetime(string="تاريخ التوريد")
    supply_end_date = fields.Datetime(string="تاريخ انتهاء التوريد")
    project_name= fields.Char(string="اسم المشروع")
    sp_notes = fields.Char(string="الملاحظات")

    def _prepare_invoice(self):
        invoice_vals = super(sale_order, self)._prepare_invoice()
        invoice_vals.update({'purchase_no': self.purchase_no or False})
        invoice_vals.update({'external_no': self.external_no or False})
        invoice_vals.update({'transaction_no': self.transaction_no or False})
        invoice_vals.update({'invoice_issue_date': self.invoice_issue_date or False})
        invoice_vals.update({'date_of_supply': self.date_of_supply or False})
        invoice_vals.update({'supply_end_date': self.supply_end_date or False})
        invoice_vals.update({'project_name': self.project_name or False})
        invoice_vals.update({'sp_notes': self.sp_notes or False})

        return invoice_vals



class AccountMove(models.Model):
    _inherit = 'account.move'

    purchase_no = fields.Char(string="رقم الشراء")
    external_no = fields.Char(string="الرقم الخارجي")
    transaction_no = fields.Char(string="رمز معاملة الفاتورة")
    invoice_issue_date = fields.Datetime(string="تاريخ اصدار الفاتورة")
    date_of_supply = fields.Datetime(string="تاريخ التوريد")
    supply_end_date = fields.Datetime(string="تاريخ انتهاء التوريد")
    project_name= fields.Char(string="اسم المشروع")
    sp_notes = fields.Char(string="الملاحظات")

