# Hospital=Staff, Patient=Member
from odoo import api, fields, models


class StaffMember(models.Model):
    _name = "staff.member"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Staff Member"

    name = fields.Char(string='Name', required=True, tracking=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: ('New'))
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    note = fields.Text(string='Description', default="New Recruit", tracking=True)
    state = fields.Selection([('draft', 'Drafted'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Canceled')],
                             default='draft', string="Status", tracking=True)
    responsible_id = fields.Many2one('res.partner', string="Responsible")
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['staff.appointment'].search_count([('member_id', '=', rec.id)])
            rec.appointment_count = appointment_count

    # @api.model
    # def create(self, vals):
    #     res = super(StaffMember, self).create(vals)
    #     print("Res ------>", res)
    #     print("vals ----->", vals)
    #     return res

    # To avoid Singleton error in odoo try to put this line in the corresponding function which contains multiple data
    # for rec in self:

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Recruit'
        if vals.get('reference', ('New')) == ('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('staff.member') or ('New')
        res = super(StaffMember, self).create(vals)
        return res

    # This function work as same for getting default values to fields
    @api.model
    def default_get(self, fields):
        res = super(StaffMember, self).default_get(fields)
        res['age'] = 20
        # res['name'] = 'John'
        # res['gender'] = 'male'
        # res['note'] = 'New Recruit'
        # res['state'] = 'draft'
        return res
