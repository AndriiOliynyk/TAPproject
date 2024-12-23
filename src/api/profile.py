from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
import json

router = APIRouter(tags=["login page"])

@router.get('/profile', response_class=HTMLResponse)
def profile():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            height: 100vh;
            background-color: #E4EAF2;
            color: #0D0D0D;
        }
        .container {
            display: flex;
            flex: 1;
        }
        .left-panel, .right-panel {
            padding: 20px;
            overflow-y: auto;
        }
        .left-panel {
            flex: 1;
            background-color: #E4EAF2;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .right-panel {
            flex: 2;
            background-color: #D6DCE5;
        }
        .profile-pic {
            position: relative;
            width: 200px;
            height: 200px;
            border-radius: 50%;
            background-color: #F2B705;
            background-size: cover;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }
        .profile-pic:hover {
            transform: scale(1.05);
        }
        .profile-pic:hover .profile-options {
            display: flex;
            opacity: 1;
        }
        .profile-options {
            position: absolute;
            bottom: -60px;
            left: 50%;
            transform: translateX(-50%);
            display: none;
            opacity: 0;
            flex-direction: column;
            gap: 10px;
            transition: opacity 0.3s ease;
        }
        .profile-options button {
            background-color: #8C1C03;
            color: #E4EAF2;
            border: none;
            padding: 10px 20px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
        }
        .profile-options button:hover {
            background-color: #F27507;
        }
        .field {
            margin-bottom: 20px;
        }
        .field label {
            font-size: 16px;
            font-weight: bold;
            display: block;
            margin-bottom: 5px;
            color: #0D0D0D; /* Чорний колір для заголовків */
        }
        .field input {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            border: 2px solid #F27507;
            border-radius: 8px;
            transition: border-color 0.3s;
            background-color: #C9D1DA; /* Темно-сірий для полів */
            color: #0D0D0D;
        }
        .field input:focus {
            border-color: #8C1C03;
            outline: none;
        }
        .payment-buttons {
            display: flex;
            gap: 10px;
        }
        .payment-buttons button {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 20px;
            background-color: #E4EAF2;
            color: #0D0D0D;
            border: 2px solid #F27507;
            border-radius: 20px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s, color 0.3s, border-color 0.3s;
        }
        .payment-buttons button img {
            width: 24px;
            height: 24px;
        }
        .payment-buttons button:hover {
            background-color: #F2B705;
            color: #0D0D0D;
            border-color: #8C1C03;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="left-panel">
            <div class="profile-pic" style="background-image: url('/static/default-profile.png');">
                <div class="profile-options">
                    <button onclick="changePhoto()">Change Photo</button>
                    <button onclick="deletePhoto()">Delete Photo</button>
                </div>
            </div>
            <h3>Favorite Photos</h3>
            <!-- Add favorite photos dynamically -->
        </div>
        <div class="right-panel">
            <div class="field">
                <label for="name">Full Name:</label>
                <input type="text" id="name" placeholder="Enter your name">
            </div>
            <div class="field">
                <label for="rental-minutes">Rental Minutes:</label>
                <input type="text" id="rental-minutes" value="0" readonly>
            </div>
            <div class="field">
                <label for="favorite-place">Favorite Place:</label>
                <input type="text" id="favorite-place" placeholder="Enter your favorite place">
            </div>
            <div class="field">
                <label>Payment Method:</label>
                <div class="payment-buttons">
                    <button onclick="setupGooglePay()">
                        <img src="/static/googlepay-logo.png" alt="Google Pay"> Google Pay
                    </button>
                    <button onclick="setupApplePay()">
                        <img src="/static/applepay-logo.png" alt="Apple Pay"> Apple Pay
                    </button>
                </div>
            </div>
        </div>
    </div>
    <script>
        function changePhoto() {
            alert("Change photo clicked!");
        }
        function deletePhoto() {
            alert("Delete photo clicked!");
        }
        function setupGooglePay() {
            alert("Google Pay setup clicked!");
        }
        function setupApplePay() {
            alert("Apple Pay setup clicked!");
        }
    </script>
</body>
</html>
"""
    return HTMLResponse(content=html_content)


# @app.post("/add_googlepay")
# def add_googlepay(user_id: int):
#     # Here you can implement logic to add Google Pay for a user
#     return JSONResponse(content={"message": f"Google Pay added for user {user_id}"})
