# Hospital=Staff, Patient=Member
from odoo import api, fields, models


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    name = fields.Char(string='Name', required=True)
    member_id = fields.Many2one('staff.member', string="Member", required=True)

    def action_create_appointment(self):
        print("Create button is clicked!")
