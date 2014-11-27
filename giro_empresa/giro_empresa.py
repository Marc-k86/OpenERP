# -*- encoding: utf-8 -*-
 
from osv import osv, fields

class res_partner_giro(osv.Model):
   _inherit = 'res.partner'
   _columns = {
               'gironegocio_id': fields.many2one('res.partner.gpro', 'Giro de Negocio'),
                  } 
res_partner_giro()
#Los Giros del Negocio del Cliente, almacenados en la BD
class res_partner_gpro(osv.Model):
   _name= 'res.partner.gpro'
   _description='Giros de Negocios del Cliente'
   _rec_name = "giro"
   _columns = {      
               'giro':fields.char('Giro', size=120, required=True),
               'cliente_ids': fields.one2many('res.partner','gironegocio_id','Cliente'),
     # ... si necesitas más campos para otros propósitos
     }
   _sql_constraints = [('giro_unico','unique(giro)','¡El Giro debe ser unica!')]
res_partner_gpro()