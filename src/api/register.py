from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
import json
import random

router = APIRouter(tags=["Create a new account"])
ID_START = pow(10, 8)
ID_END = pow(10, 9) - 1

def check_if_exist(name, email):
    with open("/home/dmytro/tap_1/TAPproject/src/api/credentials.json", "r") as file:
        content = json.load(file)
        ll = []
        try:
            for user in content["users"]:
                if (email == content["users"][user]["email"]):
                    return None
                if str(user) == (name):
                    return None
            return True
        except Exception as e:
            return e
        


@router.get("/register", response_class=HTMLResponse)
def create_new_account():
    html_content = """<!DOCTYPE html>
    <html>
    <head>
        <title>Register Page</title>
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
            <h1>Register</h1>
            <form action="/register" method="post">
                <div>
                    <label for="username">username:</label>
                    <input type="text" id="username" name="username" required>
                </div>
                <br>
                <div>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <br>
                <div>
                    <label for="email">EMAIL:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <br>
                <button type="submit">підтвердити</button>
            </form>
        </div>
    </body>
    </html>
"""
    return html_content

def create_id():
    while True:
        id = random.randint(ID_START, ID_END)
        with open("/home/dmytro/tap_1/TAPproject/src/api/credentials.json", "r") as file:
            content = json.load(file)
        for user in content["users"]:
            if content["users"][user]["id"] == id:
                continue
            else:
                return id

def write_changes(name, password, email):
    with open("/home/dmytro/tap_1/TAPproject/src/api/credentials.json", "r") as file:
        content = json.load(file)
    id = create_id()
    content["users"][name] = {
        "password": password,
        "email": email,
        "id": id
    }
    with open("/home/dmytro/tap_1/TAPproject/src/api/credentials.json", "w") as file:
        json.dump(content, file, indent=3)
    return content
@router.post('/register')
def submit_login(username: str = Form(...), password: str = Form(...), email: str = Form()):
    if len(password) < 8:
        return "the minimum lenth of password is 8 character "
    if check_if_exist(username, email) == True:
        write_changes(username, password, email)
        
        return "CREATED"
    else:
        return "username or email is already occupied"
    