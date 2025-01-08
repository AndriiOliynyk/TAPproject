from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
import json

router = APIRouter(tags=["Create a new account"])

def check_if_exist(name, email):
    with open("/home/dmytro/tap_1/TAPproject/src/api/credentials.json", "r") as file:
        content = json.load(file)
        try:
            for user in content["users"]:
                if str(content["users"][user]["email"]) == str(email):
                    return "email is already occupied"
            flag = content["users"][str(name)]
        except KeyError:
            return None
        return "nickname is already occupied"


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

def write_changes(name, password, email):
    with open("/home/dmytro/tap_1/TAPproject/src/api/credentials.json", "r") as file:
        content = json.load(file)
    content["users"][name] = {
        "password": password,
        "email": email
    }
    with open("/home/dmytro/tap_1/TAPproject/src/api/credentials.json", "w") as file:
        json.dump(content, file, indent=3)
    return content
@router.post('/register')
def submit_login(username: str = Form(...), password: str = Form(...), email: str = Form()):
    if len(password) < 8:
        return "the minimum lenth of password is 8 character "
    if check_if_exist(username, email) != None:
        return "CREATED"
        # return check_if_exist(username, email)
    
    
    write_changes(username, password, email)