from tortoise.contrib.fastapi import register_tortoise

MODELS = [
    'todo.models',
    'auth.models'
]


TORTOISE_CONFIG = {
    "connections": {"default": "sqlite://db.sqlite3"},
    "apps": {
        "models": {
            "models": [*MODELS, "aerich.models"], 
            "default_connection": "default",
        },
    },
}


def init_db(app):
    register_tortoise(
        app,
        config=TORTOISE_CONFIG,
        generate_schemas=False,
        add_exception_handlers=True,
    )

    return TORTOISE_CONFIG