import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

# 127.0.0.1:8000/todos/create/

class TodoValidate(BaseModel):
    description: str 
    is_active: Optional[bool] = False


@app.post("/todos/create/")
def create_todo_item(todo_item: TodoValidate):
    return f"description: {todo_item.description}, is_active: {todo_item.is_active}"



if __name__ == "__main__":
    uvicorn.run(app="index:app", port=8000, reload=True)