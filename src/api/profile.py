from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
import json

router = APIRouter(tags=["Profile Page"])
PATH = "/home/taras/Desktop/tap/tap1/demo-peremoga/TAPproject/src/credentials.json"

# Функція для отримання профілю з файлу за ID
def get_profile_by_id(user_id: str):
    with open(PATH, "r") as file:
        content = json.load(file)

    # ітеруємося по користувачах для пошуку за id
    for username, data in content["users"].items():
        if str(data["id"]) == user_id:
            return {"username": username, **data}

    # якщо профіль не знайдено
    raise HTTPException(status_code=404, detail="Profile not found")

def get_name():
    with open(PATH, "r") as data:
        content = json.load(data)

    usernames = list(content['users'].keys())
    return usernames

# Маршрут для сторінки профілю
@router.get("/profile/{user_id}", response_class=HTMLResponse)
def profile_page(user_id: str):
    profile = get_profile_by_id(user_id)
    usernames = get_name()  # Отримуємо всі імена користувачів
    username = profile['username']  # Беремо ім'я користувача з профілю

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Profile Page</title>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #828282;
            }}
            .main-container {{
                display: flex;
                width: 90%;
                max-width: 1400px;
                height: 600px;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
                background-color: #ffffff;
            }}
            .left-section {{
                flex: 1;
                background: url('https://img.freepik.com/free-photo/world-photography-day-celebrated-by-middle-aged-man-taking-photos-with-camera-device_23-2151672442.jpg') no-repeat center center;
                background-size: cover;
            }}
            .right-section {{
                flex: 1;
                padding: 60px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                text-align: center;
            }}
            .right-section h1 {{
                font-size: 32px;
                color: #333;
                margin-bottom: 30px;
            }}
            .form-group {{
                margin-bottom: 20px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
            label {{
                font-size: 18px;
                color: #555;
                display: block;
                font-weight: bold;
            }}
            .value {{
                font-size: 18px;
                color: #333;
            }}
            .button-group {{
                display: flex;
                justify-content: center;
                gap: 10px;
                margin-top: 10px;
            }}
            button {{
                background-color: #828282;
                color: #fff;
                font-size: 18px;
                border: none;
                padding: 12px 20px;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }}
            button:hover {{
                background-color: #004225;
            }}
            button.active {{
                background-color: #004225;
            }}
            .photo-section {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-top: 20px;
            }}
            .photo-buttons {{
                display: flex;
                gap: 10px;
            }}
            .photo-buttons button {{
                margin-left: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="main-container">
            <div class="left-section"></div>
            <div class="right-section">
                <h1>Profile page, {username}!</h1>
                <div class="form-group">
                    <label for="email">Your Email:</label>
                    <span class="value">{profile['email']}</span>
                </div>
                <div class="form-group">
                    <label for="favorite-place">Favorite Place:</label>
                    <div class="button-group">
                        <button id="place1" onclick="toggleActive('place1')">Оперний театр</button>
                        <button id="place2" onclick="toggleActive('place2')">Площа Ринок</button>
                        <button id="place3" onclick="toggleActive('place3')">Високий замок</button>
                    </div>
                </div>
                <!-- Your Photo section -->
                <div class="photo-section">
                    <label>Your Photo:</label>
                    <div class="photo-buttons">
    <button onclick="changePhoto()">Change Photo</button>
                        <button onclick="deletePhoto()">Delete Photo</button>
                    </div>
                </div>
            </div>
        </div>

        <script>
            function toggleActive(buttonId) {{
                const buttons = document.querySelectorAll('.button-group button');
                buttons.forEach(button => button.classList.remove('active'));
                document.getElementById(buttonId).classList.add('active');
            }}

            function changePhoto() {{
                alert("Change photo clicked!");
            }}

            function deletePhoto() {{
                alert("Delete photo clicked!");
            }}
        </script>
    </body>
    </html>"""
    return HTMLResponse(content=html_content)