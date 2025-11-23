from todo.models import Todo
from auth.models import User
from utils.token_manager import TokenManager
from fastapi import APIRouter, HTTPException, status, Depends
from todo.schemes import ShowTodo, TodoValidate, ChangeStatus

router = APIRouter()

# 127.0.0.1:8000/todos/create/
@router.post("/create/", status_code=status.HTTP_201_CREATED)
async def create_todo_item(todo_item: TodoValidate, user_id: int = Depends(TokenManager.get_current_user)):
    user = await  User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="İstifadəçi tapılmadı!")
    
    new_todo = await Todo.create(description=todo_item.description, is_completed=todo_item.is_completed, user=user)
    return {"detail": f"{new_todo.id} nömrəli tapşırıq əlavə edildi!"}



@router.get("/", response_model=list[ShowTodo])
async def get_todo_items(user_id: int = Depends(TokenManager.get_current_user)):

    todo_items = await Todo.filter(user=user_id)
    return todo_items


# @router.get("/{pk}", response_model=ShowTodo)
# async def get_todo_item(pk: int, user_id: int = Depends(TokenManager.get_current_user)):
#     if todo_item := await Todo.get_or_none(id=pk):
#         return todo_item
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{pk} nömrəli tapşırıq tapılmadı!")

# @router.delete('/delete/{pk}/')
# async def delete_todo_item(pk: int, user_id: int = Depends(TokenManager.get_current_user)):
#     todo_item = await Todo.get_or_none(id=pk)
#     if todo_item is not None:
#         await todo_item.delete()
#         return {"detail": f"{pk} nömrəli tapşırıq silindi!"}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{pk} nömrəli tapşırıq tapılmadı!")

# @router.delete('/delete/')
# async def delete_deactive_todo_items(user_id: int = Depends(TokenManager.get_current_user)):
#     todo_items = await Todo.filter(is_active=False)
#     for item in todo_items: 
#         await item.delete()
#     return {"detail": "Tapşırıqlar silindi!"}

# @router.patch("/update/{pk}/status/")
# async def update_todo_item(pk:int, data: ChangeStatus, user_id: int = Depends(TokenManager.get_current_user)):
#     if todo_item := await Todo.get_or_none(id=pk):
#         todo_item.is_active = data.is_active
#         await todo_item.save()
#         return {"detail":f"{pk} nömrəli tapşırığın aktivlik statusu dəyişdi."}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{pk} nömrəli tapşırıq tapılmadı!")

# @router.put("/update/{pk}/")
# async def update_todo_item(pk:int, data: TodoValidate, user_id: int = Depends(TokenManager.get_current_user)):
#     if todo_item := await Todo.get_or_none(id=pk):
#         todo_item.is_active = data.is_active
#         todo_item.description = data.description
#         await todo_item.save()
#         return {"detail":f"{pk} nömrəli tapşırıq güncəlləndi."}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"{pk} nömrəli tapşırıq tapılmadı!")
