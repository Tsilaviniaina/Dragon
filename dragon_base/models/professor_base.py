from odoo import models, fields

class Professor(models.Model):
	_inherit= 'res.partner'

	nif=fields.Char(String='NIF')
	stat=fields.Char(String='STAT')
	rcs=fields.Char(String='RCS')