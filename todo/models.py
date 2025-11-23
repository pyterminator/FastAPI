from tortoise import models, fields
from auth.models import User

class Todo(models.Model):
    id = fields.IntField(primary_key=True)

    user = fields.ForeignKeyField('models.User', related_name="todos", on_delete=fields.CASCADE)

    description = fields.TextField()
    is_completed = fields.BooleanField(default=False)