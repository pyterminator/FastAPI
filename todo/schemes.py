from pydantic import BaseModel

class CreateTodo(BaseModel):
    description: str

class UpdateTodo(BaseModel):
    description: str

class ShowTodo(BaseModel):
    id: int
    user_id: int
    description: str
    is_completed: bool

class ChangeStatus(BaseModel):
    is_completed: bool