from odoo import models, api, fields

class IrModule(models.Model):
    
    _inherit = 'ir.module.module'
    
    #----------------------------------------------------------
    # Database
    #----------------------------------------------------------
    
    active = fields.Boolean(default=True)
    #----------------------------------------------------------
    # Functions
    #----------------------------------------------------------