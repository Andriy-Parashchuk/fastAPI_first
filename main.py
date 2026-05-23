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
