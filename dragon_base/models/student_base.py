# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StudentBase(models.Model):
     _name = 'student.base'
     _description = 'Description de module'

     name = fields.Char(String='Name')
     lastname = fields.Char(String='Last name')
     birth_date=fields.Date(String='Birth date')
     age=fields.Integer(String='Age')
     matricule=fields.Char(String='Matricule')
     photo=fields.Image(String='Image')
