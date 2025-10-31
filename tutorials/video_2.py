from fastapi import FastAPI

myapp = FastAPI()

@myapp.get('/{age}')
def index(age:int):
    return {
        "name": "Mushvig",
        "age": age + 9
    }