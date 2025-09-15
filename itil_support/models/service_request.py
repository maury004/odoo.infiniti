class ServiceRequest(models.Model):
    _name = 'itil.support.service_request'
    _description = 'Service Request'

    name = fields.Char(string='Request Title', required=True)
    description = fields.Text(string='Description')
    requester_id = fields.Many2one('res.users', string='Requester', required=True)
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ], string='Status', default='new')