from tortoise import fields
from utils.hashing import Hash
from tortoise.models import Model

class User(Model):
    id = fields.IntField(primary_key=True)

    username = fields.CharField(max_length=20, unique=True)
    email = fields.CharField(max_length=50, unique=True)

    password = fields.CharField(max_length=255)


    def set_password(self, raw_password: str):
        self.password = Hash.encrypt(raw_password)

    class Meta:
        table = "users"

    