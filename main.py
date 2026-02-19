from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Endpoint GET simples 
@app.get("/")
def home():
    return {"message": "API rodando "}

    