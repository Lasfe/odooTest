# Hospital=Staff, Patient=Member
from odoo import api, fields, models


class SearchAppointmentWizard(models.TransientModel):
    _name = "search.appointment.wizard"
    _description = "Search Appointment Wizard"

    member_id = fields.Many2one('staff.member', string="Member", required=True)

    def action_search_appointment_m1(self):
        # First method for view appointments
        action = self.env["ir.actions.actions"]._for_xml_id("ab_mother.action_staff_appointment")
        action['domain'] = [('member_id', '=', self.member_id.id)]
        return action

    def action_search_appointment_m2(self):
        # Second method for view appointments
        action = self.env.ref('ab_mother.action_staff_appointment').read()[0]
        action['domain'] = [('member_id', '=', self.member_id.id)]  # To view only selected member appointments
        return action

    def action_search_appointment_m3(self):
        # Third method for view appointments
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointment',
            'res_model': 'staff.appointment',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'domain': [('member_id', '=', self.member_id.id)],
            'target': 'current',
        }
