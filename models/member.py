# Hospital=Staff, Patient=Member
from odoo import api, fields, models


class StaffMember(models.Model):
    _name = "staff.member"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Staff Member"

    name = fields.Char(string='Name', required=True, default="John", tracking=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: ('New'))
    age = fields.Char(string='Age', default="25", tracking=True)
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
        if vals.get('reference', ('New')) == ('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('staff.member') or ('New')
        res = super(StaffMember, self).create(vals)
        return res
