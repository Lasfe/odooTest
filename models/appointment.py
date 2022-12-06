# Hospital=Staff, Patient=Member
from odoo import api, fields, models


class StaffAppointment(models.Model):
    _name = "staff.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Staff Appointment"

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: ('New'))
    note = fields.Text(string='Description')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, related='member_id.gender', tracking=True)
    age = fields.Integer(string='Age', related='member_id.age', tracking=True)
    state = fields.Selection([('draft', 'Drafted'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Canceled')],
                             default='draft', string="Status", tracking=True)
    member_id = fields.Many2one('staff.member', string="Member", required=True)
    date_appointment = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Check Up Time")

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    # @api.model
    # def create(self, vals):
    #     res = super(StaffMember, self).create(vals)
    #     print("Res ------>", res)
    #     print("vals ----->", vals)
    #     return res

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Recruit'
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('staff.appointment') or ('New')
        res = super(StaffAppointment, self).create(vals)
        return res
