from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
from typing import Dict
from pydantic import BaseModel
import api.map as map, api.register as register, api.login as login

app = FastAPI()
app.include_router(map.router)
app.include_router(login.router)
app.include_router(register.router)

class RentalRequest(BaseModel):
    location: str
    duration: int

@app.get("/", response_class=HTMLResponse)
def home():
    with open("src/main.html", "r") as f:
        html_content = f.read()
    return html_content


@app.get("/location/ploscha-rynok", response_class=HTMLResponse)
def location_ploscha_rynok():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Площа Ринок - Оренда Камери</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
                color: #343a40;
            }
            h1 {
                margin-top: 20px;
                text-align: center;
            }
            .rental-options {
                text-align: center;
                margin-top: 40px;
            }
            .rental-options button {
                padding: 10px 20px;
                font-size: 16px;
                background-color: #343a40;
                color: white;
                border: none;
                cursor: pointer;
                margin: 10px;
            }
            .rental-options button:hover {
                background-color: #007bff;
            }
            footer {
                margin-top: 20px;
                padding: 10px;
                background-color: #343a40;
                color: #f8f9fa;
                text-align: center;
                position: fixed;
                width: 100%;
                bottom: 0;
            }
        </style>
    </head>
    <body>
        <h1>Оренда Камери - Площа Ринок</h1>
        <div class="rental-options">
            <h3>Доступні опції оренди:</h3>
            <button onclick="location.href='/rent?location=Площа%20Ринок&duration=10'">10 хв - 25 грн</button>
            <button onclick="location.href='/rent?location=Площа%20Ринок&duration=15'">15 хв - 35 грн</button>
            <button onclick="location.href='/rent?location=Площа%20Ринок&duration=20'">20 хв - 40 грн</button>
        </div>
        <footer>
            <p>© 2024 Оренда Камери у Львові. Всі права захищено.</p>
            <p>Адреса: Львів, вул. Шевченка, 1</p>
            <p>Телефон: +380 98 123 4567</p>
            <p>Instagram: <a href="https://instagram.com/camera_rental_lviv" target="_blank" style="color: #f8f9fa;">@camera_rental_lviv</a></p>
        </footer>
    </body>
    </html>
    """
    return html_content



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
