import uvicorn
from fastapi import FastAPI
from config import init_db
from todo.routers import router as todo_router
from auth.routers import router as auth_router


app = FastAPI()
app.include_router(todo_router, prefix="/todos")
app.include_router(auth_router, prefix="/auth")

init_db(app, ["todo.models", "auth.models"])

if __name__ == "__main__":
    uvicorn.run(app="index:app", port=8000, reload=True)