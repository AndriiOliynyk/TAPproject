from fastapi import FastAPI, HTTPException, Form, APIRouter
from fastapi.responses import HTMLResponse
from typing import List, Dict
from pydantic import BaseModel

# Define the FastAPI app
app = FastAPI()
router=APIRouter()
@router.get("/location/ploshcha-rynok", response_class=HTMLResponse)
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
                text-align: center;
            }
            h1 {
                margin-top: 100px;
            }
            .camera-gallery {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); /* Динамічне визначення колонок */
                gap: 20px; /* Проміжки між елементами */
                justify-items: center; /* Центрування зображень */
                margin-top: 40px;
                padding: 0 20px;
            }

            .camera-gallery div {
                width: 300px; /* Фіксована ширина елемента */
                text-align: center;
            }

            img {
                max-width: 100%; /* Ширина зображень не перевищує контейнер */
                height: auto; /* Автоматичне масштабування висоти */
                cursor: pointer;
                transition: transform 0.3s ease;
                margin-bottom: 10px;
            }

            img:hover {
                transform: scale(1.05); /* Збільшення зображення при наведенні */
            }


        </style>
        
    </head>
    <body>
        <h1>Оренда Камери - Площа Ринок</h1>
        
        <div class="camera-gallery">
            <div>
                 <a href="/camera1">
                <img src="https://i.moyo.ua/img/gallery/5373/2/1628542_middle.jpg" alt="Камера 1" onclick="redirectToCameraSite('camera1')">
                <p>Камера 1</p>
            </div>
            <div>
                <a href="/camera2">
                <img src="https://cdn.27.ua/sc--media--prod/default/81/36/56/813656ab-0400-41dd-8fa6-82429fb2fe44.jpg" alt="Камера 2" onclick="redirectToCameraSite('camera2')">
                <p>Камера 2</p>
            </div>
            <div>
                <a href="/camera3">
                <img src="https://volti.ua/cache/full/3216/%D0%A3%D0%A20000008N00000533141_1.jpg" alt="Камера 3" onclick="redirectToCameraSite('camera3')">
                <p>Камера 3</p>
            </div>
            <div>
                <a href="/camera4">
                <img src="https://fotosale.ua/images/products/40/products.40144.1.b.jpg" alt="Камера 4" onclick="redirectToCameraSite('camera4')">
                <p>Камера 4</p>
            </div>
            <div>
                <a href="/camera5">
                <img src="https://content1.rozetka.com.ua/goods/images/big/387827168.jpg" alt="Камера 5" onclick="redirectToCameraSite('camera5')">
                <p>Камера 5</p>
            </div>
            <div>
                <a href="/camera6">
                <img src="https://fotomost.com.ua/content/images/13/536x536l50nn0/fotoapparat-sony-zv-e10-kit-16-50mm-white-37502482939241.jpg" alt="Камера 6" onclick="redirectToCameraSite('camera6')">
                <p>Камера 6</p>
            </div>
        </div>
     
    </body>
    </html>
    """
    return html_content