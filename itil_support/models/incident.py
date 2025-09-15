class Incident(models.Model):
    _name = 'itil_support.incident'
    _description = 'Incident Management'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], string='Priority', default='medium')
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ], string='Status', default='new')