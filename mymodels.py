from tortoise import models, fields

class Todo(models.Model):
    id = fields.IntField(primary_key=True)
    description = fields.TextField()
    is_active = fields.BooleanField(default=True)