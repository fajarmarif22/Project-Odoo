from odoo import api, fields, models

class Product(models.Model):
  _inherit = 'product.product'

  course_id = fields.Many2one('training.course', string='Judul Kursus', required=True, ondelete='cascade')