from typing import List
from tortoise.contrib.fastapi import register_tortoise


# def init_db(app, models: List["str"]):
#     register_tortoise(
#         app,
#         db_url="sqlite://db.sqlite3",
#         generate_schemas=True,
#         modules={
#             "models": models
#         }
#     )

def init_db(app, models: List[str]):
    TORTOISE_CONFIG = {
        "connections": {"default": "sqlite://db.sqlite3"},  # Simple SQLite DB
        "apps": {
            "models": {
                "models": [*models, "aerich.models"], 
                "default_connection": "default",
            },
        },
    }

    register_tortoise(
        app,
        config=TORTOISE_CONFIG,
        generate_schemas=False,  # migration üçün False
        add_exception_handlers=True,
    )

    return TORTOISE_CONFIG