import uvicorn
from fastapi import FastAPI
from config import init_db
from todo.routers import router as todo_router


app = FastAPI()
app.include_router(todo_router, prefix="/todos")

init_db(app, ["todo.models"])

if __name__ == "__main__":
    uvicorn.run(app="index:app", port=8000, reload=True)