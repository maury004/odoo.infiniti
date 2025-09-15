class Problem(models.Model):
    _name = 'itil_support.problem'
    _description = 'Problem Management'

    name = fields.Char(string='Problem Title', required=True)
    description = fields.Text(string='Description')
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ], string='Status', default='new')