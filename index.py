import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from tortoise.contrib.fastapi import register_tortoise
from mymodels import Todo

app = FastAPI()

register_tortoise(
    app,
    db_url="sqlite://mydb.sqlite3",
    generate_schemas=True,
    modules={
        "models": ["mymodels"]
    }
)


class TodoValidate(BaseModel):
    description: str 
    is_active: Optional[bool] = False

# CRUD - Create

@app.post("/todos/create/")
async def create_todo_item(todo_item: TodoValidate):
    new_todo = await Todo.create(description=todo_item.description, is_active=todo_item.is_active)
    return f"Yeni item elave edildi. ID: {new_todo.id}"



if __name__ == "__main__":
    
    uvicorn.run(app, port=8000, reload=True)