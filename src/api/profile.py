from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
import json

router = APIRouter(tags=["Profile Page"])

# Функція для отримання профілю з файлу за ID
def get_profile_by_id(user_id: str):
    with open("credentials.json", "r") as file:
        content = json.load(file)

    # ітеруємося по користувачах для пошуку за id
    for username, data in content["users"].items():
        if str(data["id"]) == user_id:
            return {"username": username, **data}

    # якщо профіль не знайдено
    raise HTTPException(status_code=404, detail="Profile not found")

def get_name():
    with open("credentials.json", "r") as data:
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
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #121212;
                color: #e0e0e0;
            }}
            .container {{
                background-color: #1e1e1e;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
                padding: 30px;
                width: 400px;
                text-align: center;
            }}
            .container h1 {{
                margin-bottom: 20px;
                font-size: 24px;
                color: #bb86fc;
            }}
            .field {{
                margin: 15px 0;
                text-align: left;
            }}
            .field label {{
                display: block;
                font-weight: bold;
                margin-bottom: 5px;
                color: #e0e0e0;
            }}
            .field input {{
                width: calc(100% - 12px);
                padding: 10px;
                border: 1px solid #333;
                border-radius: 8px;
                background-color: #2c2c2c;
                color: #e0e0e0;
                outline: none;
            }}
            .field input:focus {{
                border-color: #bb86fc;
            }}
            .profile-options {{
                margin: 20px 0;
            }}
            .profile-options button {{
                background-color: #bb86fc;
                color: #121212;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
                margin: 5px;
            }}
            .profile-options button:hover {{
                background-color: #9a68df;
            }}
            .payment-buttons {{
                display: flex;
                justify-content: space-between;
                margin-top: 10px;
            }}
            .payment-buttons button {{
                display: flex;
                align-items: center;
                justify-content: center;
                background-color: #333;
                color: #e0e0e0;
                border: 1px solid #555;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
                cursor: pointer;
                flex: 1;
                margin: 5px;
            }}
            .payment-buttons button img {{
                height: 20px;
                margin-right: 8px;
            }}
            .payment-buttons button:hover {{
                background-color: #444;
                border-color: #bb86fc;
            }}
        </style>
    </head>
    <body>
    <div class="container">
            <h1>Welcome, {username}!</h1>
            <div class="profile-options">
                <button onclick="changePhoto()">Change Photo</button>
                <button onclick="deletePhoto()">Delete Photo</button>
            </div>
            <h3>Your Information</h3>
            <div class="field">
                <label for="email">Email:</label>
                <input type="email" id="email" value="{profile['email']}" readonly>
            </div>
            <div class="field">
                <label for="password">Password:</label>
                <input type="password" id="password" value="{profile['password']}" readonly>
            </div>
            <div class="field">
                <label for="favorite-place">Favorite Place:</label>
                <input type="text" id="favorite-place" placeholder="Enter your favorite place">
            </div>
            <div class="field">
                <label>Payment Method:</label>
                <div class="payment-buttons">
                    <button onclick="setupGooglePay()">
                        <img src="" alt="Google Pay"> Google Pay
                    </button>
                    <button onclick="setupApplePay()">
                        <img src="https://questfcu.com/wp-content/uploads/Apple_Pay_logo.png" alt="Apple Pay"> Apple Pay
                    </button>
                </div>
            </div>
        </div>
        <script>
            function changePhoto() {{
                alert("Change photo clicked!");
            }}
            function deletePhoto() {{
                alert("Delete photo clicked!");
            }}
            function setupGooglePay() {{
                alert("Google Pay setup clicked!");
            }}
            function setupApplePay() {{
                alert("Apple Pay setup clicked!");
            }}
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)