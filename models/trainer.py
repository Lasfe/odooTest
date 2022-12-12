# Hospital=Staff, Patient=Member, Doctor=Trainer
from odoo import api, fields, models


class StaffTrainer(models.Model):
    _name = "staff.trainer"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Staff Trainer"

    trainer_name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    note = fields.Text(string='Description')
    image = fields.Binary(string="Trainer Image")
