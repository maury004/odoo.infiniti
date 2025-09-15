class ChangeControl(models.Model):
    _name = 'itil_support.change_control'
    _description = 'Change Control'

    name = fields.Char(string='Change Control Title', required=True)
    description = fields.Text(string='Description')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft')
    created_date = fields.Datetime(string='Created Date', default=fields.Datetime.now)
    updated_date = fields.Datetime(string='Updated Date')