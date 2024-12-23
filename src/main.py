from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
from typing import Dict
from pydantic import BaseModel

app = FastAPI()


class RentalRequest(BaseModel):
    location: str
    duration: int

@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Оренда Камери у Львові</title>
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
            nav {
                background-color: #343a40;
                color: #f8f9fa;
                padding: 20px 20px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            nav .logo {
                font-size: 1.5em;
                font-weight: bold;
            }
            nav a {
                color: #f8f9fa;
                text-decoration: none;
                margin: 0 10px;
            }
            nav a:hover {
                text-decoration: underline;
            }

            nav .right-links {
            display: flex;
                justify-content: flex-end;
            }
            form {
                margin: 20px auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                display: inline-block;
                text-align: center;
            }
            label, select, button {
                display: block;
                margin: 10px 0;
            }
            .image-gallery {
                display: flex;
                justify-content: space-around;
                gap: 20px;
                margin-top: 40px;
            }
            .image-gallery div {
                text-align: center;
            }
            img {
                max-width: 650px;
                height: 450px;
                cursor: pointer;
                transition: transform 0.3s ease;
            }
            img:hover {
                transform: scale(1.05);  
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
        <nav>
            <div class="logo">Лого</div>
            <div>
                <a href="#">Головна</a>
                <a href="#">Карта</a>
                <a href="#">Увійти</a>
                <a href="#">Реєстрація</a>
                <a href="#">Профіль</a>
            </div>
        </nav>
        <h1>Оренда Камери у Львові</h1>

        <!-- Image Section for Locations -->
        <div class="image-gallery">
            <div>
                <h3>Площа Ринок</h3>
                <a href="/location/ploscha-rynok">
                <img src="https://ua.igotoworld.com/frontend/webcontent/images/tours/1035068_800x600_aerophoto_lviv_9.jpg" alt="Площа Ринок" />
                </a>
            </div>
            <div>
                <h3>Оперний театр</h3>
                <a href="/location/opernyi-teatr">
                <img src="https://karpatium.com.ua/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBbFlOIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--f98bbf8449e179039f6387a8832be7980b61ac53/%D0%9E%D0%BF%D0%B5%D1%80%D0%BD%D0%B8%D0%B8%CC%86%20%D1%82%D0%B5%D0%B0%D1%82%D1%80%20%D1%83%20%D0%9B%D1%8C%D0%B2%D0%BE%D0%B2%D1%96.jpeg" alt="Оперний театр" />
                </a>
            </div>
            <div>
                <h3>Високий замок</h3>
                <a href="/location/vysokyi-zamok">
                <img src="https://travels.in.ua/api/Photo/PhotoStreamCPOI/37125" alt="Високий замок" />
                </a>
            </div>
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
