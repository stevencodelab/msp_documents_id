from odoo import models, api, fields, _
from odoo.exceptions import UserError, AccessError, ValidationError
import datetime


class MspDocumentsId(models.Model):
    _name = 'msp.documents.id'
    _description = 'MSP Documents ID'

    documents_id = fields.Char(string="Documents ID", store=True, copy=False, readonly=False)
    revision_date = fields.Datetime(string="Revision Date", readonly=False)
    effective_date = fields.Datetime(string="Effective Date", readonly=False, store=True)

