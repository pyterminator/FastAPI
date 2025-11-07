from typing import List
from tortoise.contrib.fastapi import register_tortoise


def init_db(app, models: List["str"]):
    register_tortoise(
        app,
        db_url="sqlite://db.sqlite3",
        generate_schemas=True,
        modules={
            "models": models
        }
    )