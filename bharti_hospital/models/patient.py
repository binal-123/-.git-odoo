from odoo import models, fields


class HospitalPatient(models.Model):
    _name="hospital.patient"
    _descrpition='This model will store the data of our hospital staff and patients.'

    name=fields.Char(string="Name")
    age=fields.Integer(string="AGE")
    dob=fields.Date(string="DOB")
    mobile=fields.Integer(string="Mobile")
    email=fields.Char(string="Email")
    city=fields.Char(string="City")


