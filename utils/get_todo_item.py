from auth.models import User
from todo.models import Todo
from utils.token_manager import TokenManager
from fastapi import Depends, HTTPException, status

async def get_todo_item(pk: int, user: User = Depends(TokenManager.get_current_user)):
    todo_item = await Todo.get_or_none(id=pk)

    if not todo_item or (todo_item.user_id != user.id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tapılmadı")

    return todo_item

