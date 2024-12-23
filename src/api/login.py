from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
import json

router = APIRouter(tags=["login page"])

@router.get('/login', response_class=HTMLResponse)
def login():
        html_content = """<!DOCTYPE html>
    <html>
    <head>
        <title>Login Page</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
            }
            .container {
                text-align: center;
                border: 1px solid #ccc;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            form {
                display: inline-block;
            }
            label, input, button {
                font-size: 16px;
            }
            button {
                margin-top: 10px;
                padding: 5px 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Login</h1>
            <form action="/submit-login" method="post">
                <div>
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>
                </div>
                <br>
                <div>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <br>
                <button type="submit">підтвердити</button>
            </form>
        </div>
    </body>
    </html>
"""
        return html_content


def check_login(password, login):
    with open("/home/dmytro/tap_1/TAPproject/src/api/credentials.json", "r") as file:
        content = json.load(file)
    try:
        for user in content["users"]:
            if content["users"][user]["email"] == login:
                login = user
        if str(password) != str(content["users"][str(login)]["password"]):
    
            return "wrong password or login"
        else:
            return "success"
    except KeyError:
        return "wrong password or login"

@router.post('/submit-login')
def submit_login(username: str = Form(...), password: str = Form(...)):
    if len(password) < 8:
        return "the minimum lenth of password is 8 character "
    return check_login(password, username)
    


    
