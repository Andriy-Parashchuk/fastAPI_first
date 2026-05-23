from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Union

# Створення екземпляру FastAPI
app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    email: str


users = []


@app.post('/create_user')
def add_entity(user: User):
    users.append(user)
    return user


@app.get("/users/")
def get_all_users():
    return users


@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    for u in users:
        if user_id == u.id:
            return u
    return 'такого немає'

