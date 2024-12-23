from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
from typing import Dict
from pydantic import BaseModel

app = FastAPI()

locations = {
    "Площа Ринок": "https://example.com/ploscha-rynok.jpg",
    "Оперний театр": "https://example.com/opernyi-teatr.jpg",
    "Високий замок": "https://example.com/vysokyi-zamok.jpg"
}
rates = {
    10: 25,
    15: 35,
    25: 40
}

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
                text-align: center;
            }
            h1 {
                margin-top: 20px;
            }
            form {
                margin: 20px auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }
            label, select, button {
                display: block;
                margin: 10px 0;
            }
            img {
                max-width: 300px;
                height: auto;
                margin-top: 20px;
            }
            footer {
                margin-top: 20px;
                padding: 10px;
                background-color: #343a40;
                color: #f8f9fa;
                position: fixed;
                width: 100%;
                bottom: 0;
            }
        </style>
    </head>
    <body>
        <h1>Оренда Камери у Львові</h1>
        <form action="/rent" method="post">
            <label for="location">Виберіть локацію:</label>
            <select name="location" id="location" onchange="updateImage()">
                <option value="Площа Ринок">Площа Ринок</option>
                <option value="Оперний театр">Оперний театр</option>
                <option value="Високий замок">Високий замок</option>
            </select>
            <br><br>
            <label for="duration">Виберіть тривалість (хвилин):</label>
            <select name="duration" id="duration">
                <option value="10">10 хвилин - 25 грн</option>
                <option value="15">15 хвилин - 35 грн</option>
                <option value="25">25 хвилин - 40 грн</option>
            </select>
            <br><br>
            <button type="submit">Орендувати</button>
        </form>
        <img id="locationImage" src="https://example.com/ploscha-rynok.jpg" alt="Локація">
        <footer>
            <p>© 2024 Оренда Камери у Львові. Всі права захищено.</p>
            <p>Адреса: Львів, вул. Шевченка, 1</p>
            <p>Телефон: +380 98 123 4567</p>
            <p>Instagram: <a href="https://instagram.com/camera_rental_lviv" target="_blank" style="color: #f8f9fa;">@camera_rental_lviv</a></p>
        </footer>
        <script>
            const locations = {
                "Площа Ринок": "https://example.com/ploscha-rynok.jpg",
                "Оперний театр": "https://example.com/opernyi-teatr.jpg",
                "Високий замок": "https://example.com/vysokyi-zamok.jpg"
            };

            function updateImage() {
                const select = document.getElementById('location');
                const image = document.getElementById('locationImage');
                image.src = locations[select.value];
            }
        </script>
    </body>
    </html>
    """
    return html_content

@app.post("/rent")
def rent_camera(location: str = Form(...), duration: int = Form(...)):
    if location not in locations:
        raise HTTPException(status_code=400, detail="Невірна локація.")
    if duration not in rates:
        raise HTTPException(status_code=400, detail="Невірна тривалість.")

    cost = rates[duration]
    return {
        "message": f"Камеру успішно орендовано на {duration} хвилин у локації '{location}'.",
        "cost": f"Вартість: {cost} грн.",
        "location_image": locations[location]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)