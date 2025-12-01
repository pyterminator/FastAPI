from todo.models import Todo
from auth.models import User
from utils.token_manager import TokenManager
from utils.get_todo_item import get_todo_item as gti
from fastapi import APIRouter, HTTPException, status, Depends
from todo.schemes import ShowTodo, CreateTodo, ChangeStatus, UpdateTodo

router = APIRouter()

@router.post("/create/", status_code=status.HTTP_201_CREATED, response_model=ShowTodo)
async def create_todo_item(todo_item: CreateTodo, user: User = Depends(TokenManager.get_current_user)):
    try: 
        new_todo = await Todo.create( description=todo_item.description, user=user)
    except: 
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail="Todo item əlavə edilərkən problem oldu")

    return new_todo

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ShowTodo])
async def get_todo_items(user: User = Depends(TokenManager.get_current_user)):
    return await Todo.filter(user=user).all()

@router.get("/{pk}", status_code=status.HTTP_200_OK, response_model=ShowTodo)
async def get_todo_item(todo_item: Todo = Depends(gti)): 
    return todo_item

@router.delete('/delete/{pk}/', status_code=status.HTTP_200_OK)
async def delete_todo_item(pk: int, todo_item: Todo = Depends(gti)):
    try: 
        await todo_item.delete()
    except: 
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail="Silinmə prosesində xəta oldu")

    return { "detail" : f"ID={pk} nömrəli tapşırıq silindi!" }

@router.delete('/delete/', status_code=status.HTTP_200_OK)
async def delete_all_my_todo_items(user: User = Depends(TokenManager.get_current_user)):
    user_todo_items = await Todo.filter(user=user).all()
    try: 
        for item in user_todo_items: 
            await item.delete()
    except:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail="Silinmə prosesində xəta oldu")

    return {"detail": "Tapşırıqlar silindi"}

@router.patch("/update/{pk}/status/", status_code=status.HTTP_200_OK, response_model=ShowTodo)
async def update_todo_item(data: ChangeStatus, todo_item: Todo = Depends(gti)):
    try:
        todo_item.is_completed = data.is_completed
        await todo_item.save()
    except:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail = f"Status dəyişdirmə prosesində xəta oldu")

    return todo_item

@router.patch("/update/{pk}/", status_code=status.HTTP_200_OK, response_model=ShowTodo)
async def update_todo_item(data: UpdateTodo, todo_item: Todo = Depends(gti)):
    try:
        todo_item.description = data.description
        await todo_item.save()
    except:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail = f"Güncəlləmə prosesində xəta oldu")

    return todo_item
