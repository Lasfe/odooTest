# Hospital=Staff, Patient=Member, Doctor=Trainer
from odoo import api, fields, models


class StaffAppointment(models.Model):
    _name = "staff.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Staff Appointment"
    _order = "trainer_id,name,note desc"  # (desc for Descreasing order, asc for Ascending order)

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                       default=lambda self: ('New'))
    note = fields.Text(string='Description')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string="Gender")
    age = fields.Integer(string='Age', related='member_id.age', tracking=True)
    state = fields.Selection([('draft', 'Drafted'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Canceled')],
                             default='draft', string="Status", tracking=True)
    member_id = fields.Many2one('staff.member', string="Member", required=True)
    trainer_id = fields.Many2one('staff.trainer', string="Trainer", required=True)
    instruction_line_ids = fields.One2many('appointment.instruction.lines', 'appointment_id', string="Instruction Lines")
    # Many2one fields must end with _id syntax !
    # One2many fields must end with _ids syntax !
    date_appointment = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Check Up Time")
    instruction = fields.Text(string='Instruction')


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

    @api.onchange('member_id')
    def onchange_member_id(self):
        if self.member_id:
            if self.member_id.gender:
                self.gender = self.member_id.gender
            if self.member_id.note:
                self.note = self.member_id.note

        else:
            self.gender = ''
            self.note = ''


class AppointmentInstructionLines(models.Model):
    _name = "appointment.instruction.lines"
    _description = "Appointment Instruction Lines"

    name = fields.Char(string="Equipment", required=True)
    qty = fields.Integer(string="Quantity", required=True)
    appointment_id = fields.Many2one('staff.appointment', string="Appointment")
# New model for instruction lines. Is this an alternative method for define a new model?
# But remember that you need to add access for this new model in the security directory
