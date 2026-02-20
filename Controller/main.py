from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Endpoint GET simples 
@app.post("/api/auth/register")


def register(data: UserRegisterDTO):
    user_service = UserService()
    

    return user_service.register(data.email, data.password)