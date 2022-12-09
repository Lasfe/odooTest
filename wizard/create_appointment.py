# Hospital=Staff, Patient=Member
from odoo import api, fields, models


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    date_appointment = fields.Date(string='Date', required=False)
    member_id = fields.Many2one('staff.member', string="Member", required=True)

    def action_create_appointment(self):
        # print("Create button is clicked!")
        vals = {
            'date_appointment': self.date_appointment,
            'member_id': self.member_id.id
        }
        appointment_rec = self.env['staff.appointment'].create(vals)
        print("Appointment ID ------>", appointment_rec.id)
        return {
            'name': 'Appointment',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'staff.appointment',
            'res_id': appointment_rec.id,
            # 'target': 'new',  # Add this line if you want to see the new appointment in pop-up view
        }

    def action_view_appointment(self):
        # First method for view appointments
        action = self.env["ir.actions.actions"]._for_xml_id("ab_mother.action_staff_appointment")
        action['domain'] = [('member_id', '=', self.member_id.id)]
        return action

        # Second method
        # action = self.env.ref('ab_mother.action_staff_appointment').read()[0]
        # action['domain'] = [('member_id', '=', self.member_id.id)]  # To view only selected member appointments
        # return action

        # Third method
        # return {
        #     'type': 'ir.actions.act_window',
        #     'name': 'Appointment',
        #     'res_model': 'staff.appointment',
        #     'view_type': 'form',
        #     'view_mode': 'tree,form',
        #     'domain': [('member_id', '=', self.member_id.id)],
        #     'target': 'current',
        # }
