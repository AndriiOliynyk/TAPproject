from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse

# Define the FastAPI app
app = FastAPI()
router=APIRouter()
@router.get("/camera3", response_class=HTMLResponse)
def camera_details():
    camera_name = "Nikon D850 + Nikon AF-S 24-70 мм f/2.8E ED VR "
    image_url = "https://s.ek.ua/jpg_zoom1/1192559.jpg"
    description = """Camera Body (Nikon D850):
Sensor: 45.7 MP full-frame CMOS sensor (FX format) with no optical low-pass filter for stunning detail and sharpness.
ISO Range: 64-25,600 (expandable to 32-102,400) for superior performance in low-light conditions.
Autofocus: 153-point AF system with 99 cross-type sensors for fast, accurate focusing.
Video Recording: 4K UHD at 30/25/24 fps, with full HD at 120 fps for slow motion.
Screen: 3.2-inch tilting touchscreen LCD with 2.36M dots.
Lens (Nikon AF-S 24-70mm f/2.8E ED VR):
Focal Length: 24-70mm, ideal for landscapes, portraits, and events.
Maximum Aperture: f/2.8 constant across the zoom range for excellent low-light performance and shallow depth of field.
Vibration Reduction (VR): Up to 4 stops of stabilization for sharper handheld shots.
Optics: Extra-low Dispersion (ED) and Aspherical elements for reduced aberrations and outstanding clarity.
"""
    rating = 4.5  # Рейтинг з 5

    # Різні варіанти ціни за оренду
    prices = {
        "10 хв": 10,
        "15 хв": 20,
        "20 хв": 40
    }

    rating = 5  # Фіксований рейтинг
    full_stars = "★" * rating  # Заповнені зірочки
    empty_stars = "☆" * (5 - rating)  # Порожні зірочки
    star_rating = full_stars + empty_stars

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{camera_name} - Деталі Камери</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
                color: #343a40;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .camera-details {{
                display: flex;
                flex-direction: column;
                align-items: center;
                width: 80%;
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            .content {{
                display: flex;
                justify-content: space-between;
                width: 100%;
                gap: 20px;
                margin-bottom: 20px;
            }}
            .left-side {{
                max-width: 50%;
                text-align: left;
            }}
            .right-side {{
                max-width: 40%;
                text-align: left;
            }}
            img {{
                width: 100%;
                height: auto;
                border-radius: 8px;
            }}
            .description {{
                font-size: 16px;
                margin-top: 20px;
                white-space: pre-line; /* Зберігаємо розриви рядків */
                line-height: 1.6; /* Відстань між рядками */
            }}
            .rating {{
                margin-top: 20px;
                font-size: 24px; /* Більші шрифти для рейтингу */
                color: #f39c12;
            }}
            .price {{
                font-size: 20px;
                margin-top: 20px;
                font-weight: bold;
            }}
            .price-list {{
                margin-top: 20px;
                font-size: 18px;
                display: flex;
                gap: 15px;
            }}
            .price-button {{
                background-color: #6c757d;
                color: white;
                padding: 15px 25px;
                font-size: 20px;
                border: none;
                cursor: pointer;
                border-radius: 5px;
                transition: background-color 0.3s;
                width: 100%;
                text-align: center;
            }}
            .price-button:hover {{
                background-color: #5a6268;
            }}
            .price-button.selected {{
                background-color: #007542;
            }}
            .button-container {{
                display: flex;
                justify-content: space-between;
                width: 100%;
                gap: 20px;
                margin-top: 20px;
            }}
            .rental-btn {{
                background-color: #6c757d;
                color: white;
                padding: 15px 25px;
                font-size: 20px;
                border: none;
                cursor: pointer;
                border-radius: 5px;
                width: 100%;
                text-align: center;
                transition: background-color 0.3s;
            }}
            .rental-btn.show {{
                background-color: #004225;
            }}
        </style>
        <script>
            function selectPrice(button, price) {{
                var buttons = document.querySelectorAll('.price-button');
                buttons.forEach(function(b) {{
                    b.classList.remove('selected');
                }});
                button.classList.add('selected');

                document.getElementById('rental-btn').classList.add('show');
                document.getElementById('rental-btn').onclick = function() {{
                    window.location.href = '/rent?camera={camera_name}&price=' + price;
                }};
            }}
        </script>
    </head>
    <body>
        <div class="camera-details">
            <div class="content">
                <div class="left-side">
                    <h1>{camera_name}</h1>
                    <p class="description">{description}</p>
                    <p class="rating">Рейтинг: {star_rating}</p>
                </div>
                <div class="right-side">
                    <img src="{image_url}" alt="{camera_name}">
                </div>
            </div>
            <div class="price-list">
                <button class="price-button" onclick="selectPrice(this, {prices['10 хв']})">10 хв - {prices['10 хв']} грн</button>
                <button class="price-button" onclick="selectPrice(this, {prices['15 хв']})">15 хв - {prices['15 хв']} грн</button>
                <button class="price-button" onclick="selectPrice(this, {prices['20 хв']})">20 хв - {prices['20 хв']} грн</button>
            </div>
            <div class="button-container">
                <button class="rental-btn" id="rental-btn">Забронювати</button>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content