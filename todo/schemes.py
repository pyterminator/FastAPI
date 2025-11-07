from pydantic import BaseModel
from typing import Optional

class TodoValidate(BaseModel):
    description: str 
    is_active: Optional[bool] = True

class ShowTodo(BaseModel):
    id: int
    description: str
    is_active: bool

class ChangeStatus(BaseModel):
    is_active: bool