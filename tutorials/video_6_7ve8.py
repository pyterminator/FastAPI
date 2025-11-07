# import uvicorn
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional
# from tortoise.contrib.fastapi import register_tortoise
# from mymodels import Todo

# app = FastAPI()

# register_tortoise(
#     app,
#     db_url="sqlite://mydb.sqlite3",
#     generate_schemas=True,
#     modules={
#         "models": ["mymodels"]
#     }
# )


# class TodoValidate(BaseModel):
#     description: str 
#     is_active: Optional[bool] = True

# class ShowTodo(BaseModel):
#     description: str
#     is_active: bool

# class ChangeStatus(BaseModel):
#     is_active: Optional[bool]

# # CRUD - Create Read Update (PUT, PATCH) Delete

# @app.post("/todos/create/")
# async def create_todo_item(todo_item: TodoValidate):
#     new_todo = await Todo.create(description=todo_item.description, is_active=todo_item.is_active)
#     return f"Yeni item elave edildi. ID: {new_todo.id}"


# # 127.0.0.1:8000/todos/

# @app.get("/todos/", response_model=list[ShowTodo])
# async def get_todo_items():
#     todo_items = await Todo.all()
#     return todo_items

# @app.get("/todos/{pk}", response_model=ShowTodo)
# async def get_todo_item(pk: int):
#     if todo_item := await Todo.filter(id=pk).first():
#         return todo_item
    
#     # if todo_item := await Todo.get_or_none(id=pk):
#     #     return todo_item
#     return {"error": "Todo item - tapilmadi!"}
    

# @app.delete('/todos/delete/{pk}/')
# async def delete_todo_item(pk: int):
#     todo_item = await Todo.get_or_none(id=pk)
#     if todo_item is not None:
#         await todo_item.delete()
#         return {"message": f"{pk} nomreli todo item silindi!"}
#     return {"error":"Todo item - tapilmadi!"}

# @app.delete('/todos/delete/')
# async def delete_deactive_todo_items():
#     todo_items = await Todo.filter(is_active=False)
#     for item in todo_items: await item.delete()
#     return {"message": "Todo itemlar silindi!"}

# @app.patch("/todos/update/{pk}/status/")
# async def update_todo_item(pk:int, data: ChangeStatus):
#     if todo_item := await Todo.get_or_none(id=pk):
#         todo_item.is_active = data.is_active
#         await todo_item.save()
#         return {"message":f"{pk} nomreli todo item statusu deyisdi."}
#     return {"error":"Todo item - tapilmadi!"}


# @app.put("/todos/update/{pk}/")
# async def update_todo_item(pk:int, data: TodoValidate):
#     if todo_item := await Todo.get_or_none(id=pk):
#         todo_item.is_active = data.is_active
#         todo_item.description = data.description
#         await todo_item.save()
#         return {"message":f"{pk} nomreli todo item guncellendi."}
#     return {"error":"Todo item - tapilmadi!"}

# if __name__ == "__main__":
#     uvicorn.run(app="index:app", port=8000, reload=True)