from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse

app = FastAPI()
router=APIRouter()
@router.get("/map", response_class=HTMLResponse)
async def home_page():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Головна сторінка</title>
        <style>
            body, html {
                height: 100%;
                margin: 0;
                padding: 0;
            }
            #map {
                height: 100vh;  /* Встановлено висоту на 100% від вікна браузера */
                width: 100%;  /* Встановлено ширину на 100% */
            }
        </style>
        <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                var map = L.map('map').setView([49.843634, 24.026460], 14);  // Центр карти

                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                }).addTo(map);

                // Локації
                var locations = [
                    {
                        lat: 49.843634, 
                        lng: 24.026460, 
                        title: "Оперний театр", 
                        link: "https://maps.app.goo.gl/jy8CmZWWyZn9uRdJA"
                    },
                    {
                        lat: 49.848931, 
                        lng: 24.033526, 
                        title: "Високий Замок", 
                        link: "https://maps.app.goo.gl/SeBFp97xHzBNJAxA9"
                    },
                    {
                        lat: 49.841562, 
                        lng: 24.032331, 
                        title: "Площа Ринок", 
                        link: "https://maps.app.goo.gl/ezYJEonHnrHDTpYU8"
                    }
                ];

                // Додавання маркерів
                locations.forEach(function(location) {
                    L.marker([location.lat, location.lng])
                        .addTo(map)
                        .bindPopup('<a href="' + location.link + '" target="_blank">' + location.title + '</a>');  // Посилання відкривається в новій вкладці
                });
            });
        </script>
    </head>
    <body>
        <div id="map"></div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)