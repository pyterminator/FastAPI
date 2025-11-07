# import uvicorn
# from fastapi import FastAPI
# from typing import Optional

# app = FastAPI()

# # 127.0.0.1:8000/users

# users_list = [
#     {
#         "id":1,
#         "name":"Mushvig",
#         "age": 23
#     },
#     {
#         "id":2,
#         "name":"Eyvaz",
#         "age": 22
#     },
#     {
#         "id":3,
#         "name":"Natiq",
#         "age": 19
#     }
# ]


# @app.get('/users')
# def users(id:Optional[int]=None, age:int|None=None):
#     if id and age:
#         new_users = []
#         for user in users_list:
#             if user.get('id') == id: new_users.append(user)
#             if user.get("age") == age: new_users.append(user)
#         return new_users
#     if id:
#         for user in users_list:
#             if user.get('id') == id:
#                 return user
#         return "Not found!!"
#     if age:
#         for user in users_list:
#             if user.get('age') == age:
#                 return user
#         return "Not found!!"
#     return users_list

# if __name__ == "__main__":
#     uvicorn.run(app="index:app", port=9000, reload=True, host="127.1.1.1")