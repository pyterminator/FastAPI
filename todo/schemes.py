from pydantic import BaseModel
from typing import Optional

class TodoValidate(BaseModel):
    description: str 
    is_completed: Optional[bool] = False

class ShowTodo(BaseModel):
    id: int
    description: str
    is_completed: bool

class ChangeStatus(BaseModel):
    is_completed: bool