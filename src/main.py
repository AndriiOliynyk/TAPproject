from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
from typing import Dict
from pydantic import BaseModel

app = FastAPI()

locations = ["Площа Ринок", "Оперний театр", "Високий замок"]
rates = {
    10: 25,
    15: 35,
    25: 40
}

class RentalRequest(BaseModel):
    location: str
    duration: int

@app.get("/")
def read_root():
    return {"Hello": "World"}