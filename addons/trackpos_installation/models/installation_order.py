from odoo import models, fields

class InstallationOrder(models.Model):
    _name = 'installation.order'
    _description = 'Orden de Instalación GPS'

    name = fields.Char(string='Referencia', required=True, default='Nueva')
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    vehicle =   fields.Char(string='Vehículo', required=True)
    product_id = fields.Many2one('product.product', string='Dispositivo', required=True)
    location = fields.Text(string='Ubicación o coordenadas')
    technician_id = fields.Many2one('hr.employee', string='Técnico asignado', required=True)
    scheduled_date = fields.Datetime(string='Fecha estimada')
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('assigned', 'Asignada'),
        ('installed', 'Instalado')
    ], default='pending', string='Estado')
    notes = fields.Text(string='Observaciones')

    def name_get(self):
        return [(record.id, f"{record.name} - {record.partner_id.name}") for record in self]