from fastapi import FastAPI
from pydantic import BaseModel

class UserRegisterDTO(BaseModel):
    email: str
    password: str

    