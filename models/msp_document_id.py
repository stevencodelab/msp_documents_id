from odoo import models, api, fields, _
from odoo.exceptions import UserError, AccessError, ValidationError
import datetime


class MspDocumentsId(models.Model):
    _name = 'msp.documents.id'
    _description = 'MSP Documents ID'

    documents_id = fields.Char(string="Documents ID", store=True, copy=False, readonly=False)
    revision_date = fields.Datetime(string="Revision Date", readonly=False)
    effective_date = fields.Datetime(string="Effective Date", readonly=False, store=True)

    state = fields.Selection([
            ('draft','Draft'),
            ('confirmed','Confirmed'),
            ('cancel', 'Cancelled')], 
            string="Status", readonly=True,copy=False, default="draft",track_visibility='onchange', widget='statusbar')  

    # Tombol Draft
    def action_draft(self):
        self.write({'state': 'draft'}) 
    # Tombol start
    def action_confirmed(self):
        self.write({'state': 'confirmed'})
    # Tombol Cancel
    def action_cancel(self):
        self.write({'state': 'cancel'})       

    def name_get(self):
        result = [] 
        for record in self:
            id = record.documents_id 
            result.append((record.id, id))
        return result                     
    