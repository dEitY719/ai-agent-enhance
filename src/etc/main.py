from fastapi import FastAPI
from models import User, UserCreate

app = FastAPI()

@app.get("/users", response_model=list[User])
def list_users():
    return [User(id=1, name="Alice")]

@app.post("/users", response_model=User, status_code=201)
def create_user(user: UserCreate):
    return User(id=2, name=user.name)
