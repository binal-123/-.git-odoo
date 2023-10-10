from odoo import models, fields


class WitsonStudent(models.Model):
    _name="witson.student"
    _description="All the records of the university are here."


    name=fields.Char(string="name")
    std=fields.Integer(string="std")
    div=fields.Char(string="div")



class StudentDetail(models.Model):
    _name="student.detail"
    _description="All the details of the students are here."

    name=fields.Char(string="name")
    add=fields.Char(string="add")
    mobile=fields.Integer(string="mobile")
    group=fields.Char(string="group")
