from odoo import models, fields, api

class StudentClass(models.Model):
    _name = 'student.class'
    _description= 'Student class'

    name=fields.Char(String='Name')
    student_number=fields.Integer(String='Student number')
    stage=fields.Char(String='Stage')
