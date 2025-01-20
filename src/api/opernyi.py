from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse

app = FastAPI()
router=APIRouter()
@router.get("/location/opernyi-teatr", response_class=HTMLResponse)
def location_opernyi():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Оперний театр - Оренда Камери</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #ffffff;
                color: #343a40;
                text-align: center;
            }
            h1 {
                margin-top: 100px;
            }
            .camera-gallery {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
                gap: 20px;
                justify-items: center;
                margin-top: 40px;
                padding: 0 20px;
            }
            .camera-gallery div {
                width: 300px;
                text-align: center;
            }
            img {
                max-width: 100%;
                height: auto;
                cursor: pointer;
                transition: transform 0.3s ease;
                margin-bottom: 10px;
            }
            img:hover {
                transform: scale(1.05);
            }
            button {
                background-color: #6c757d;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 14px;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            button:hover {
                background-color: #004225;
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
        </style>
    </head>
    <body>
        <nav>
            <div class="logo">Лого</div>
            <div>
                <a href="/">Головна</a>
                <a href="/map">Карта</a>
                <a href="/login">Увійти</a>
                <a href="/register">Реєстрація</a>
                <a href="/profile/{user_id}">Профіль</a>
            </div>
        </nav>
        <h1>Оренда Камери - Оперний театр </h1>
        <div class="camera-gallery">
            <div>
                <img src="https://i.moyo.ua/img/gallery/5373/2/1628542_middle.jpg" alt="Камера 1">
                <p>Canon Digital camera EOS R50</p>
                <button onclick="window.location.href='/camera1'">Забронювати</button>
            </div>
            <div>
                <img src="https://cdn.27.ua/sc--media--prod/default/81/36/56/813656ab-0400-41dd-8fa6-82429fb2fe44.jpg" alt="Камера 2">
                <p>Fujifilm INSTAX Mini 12 </p>
                <button onclick="window.location.href='/camera2'">Забронювати</button>
            </div>
            <div>
                <img src="https://volti.ua/cache/full/3216/%D0%A3%D0%A20000008N00000533141_1.jpg" alt="Камера 3">
                <p>Nikon D850 + Nikon AF-S 24-70 мм f/2.8E ED VR</p>
                <button onclick="window.location.href='/camera3'">Забронювати</button>
            </div>
            <div>
                <img src="https://fotosale.ua/images/products/40/products.40144.1.b.jpg" alt="Камера 4">
                <p>Sony Cyber-shot DSC-RX10 IV Digital Camera</p>
                <button onclick="window.location.href='/camera4'">Забронювати</button>
            </div>
            <div>
                <img src="https://content1.rozetka.com.ua/goods/images/big/387827168.jpg" alt="Камера 5">
                <p>SONY ZV-1F Black</p>
                <button onclick="window.location.href='/camera5'">Забронювати</button>
            </div>
            <div>
                <img src="https://fotomost.com.ua/content/images/13/536x536l50nn0/fotoapparat-sony-zv-e10-kit-16-50mm-white-37502482939241.jpg" alt="Камера 6">
                <p>Sony ZV-E10 Kit 16-50mm f3.5-5.6 OSS</p>
                <button onclick="window.location.href='/camera6'">Забронювати </button>
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

app.include_router(router)
