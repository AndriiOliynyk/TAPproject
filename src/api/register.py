from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
import json
import random

PATH = "/home/taras/Desktop/tap/tap1/demo-peremoga/TAPproject/src/credentials.json"

router = APIRouter(tags=["Create a new account"])
ID_START = pow(10, 8)
ID_END = pow(10, 9) - 1

def check_if_exist(name, email):
    with open(PATH, "r") as file:
        content = json.load(file)
        try:
            for user in content["users"]:
                if email == content["users"][user]["email"] or str(user) == name:
                    return None
            return True
        except Exception as e:
            return e

from fastapi.responses import HTMLResponse

@router.get("/register", response_class=HTMLResponse)
def create_new_account(error_message: str = None):
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Register Page</title>
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
            background: url('https://i0.wp.com/digital-photography-school.com/wp-content/uploads/2024/02/how-to-become-a-good-photographer-105.jpg?resize=1500%2C1000&ssl=1') no-repeat center center;
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
        }}
        label {{
            font-size: 18px;
            color: #555;
            display: block;
            margin-bottom: 8px;
        }}
        input {{
            width: 100%;
            padding: 12px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        button {{
            background-color: #ccc;
            color: #fff;
            font-size: 18px;
            border: none;
            padding: 12px 20px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-top: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        button:hover {{
            background-color: #004225;
        }}
        .error-message {{
            color: red;
            margin-top: 10px;
            font-size: 16px;
        }}
    </style>
</head>
<body>
    <div class="main-container">
        <div class="left-section"></div>
        <div class="right-section">
            <h1>Register</h1>
            <form action="/register" method="post">
                <div class="form-group">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>
                </div>
                <div class="form-group">
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <button type="submit">Підтвердити</button>
                {f'<p class="error-message">{error_message}</p>' if error_message else ''}
            </form>
        </div>
    </div>
</body>
</html>
"""
    return HTMLResponse(content=html_content)



def create_id():
    while True:
        id = random.randint(ID_START, ID_END)
        with open(PATH, "r") as file:
            content = json.load(file)
        for user in content["users"]:
            if content["users"][user]["id"] == id:
                break
        else:
            return id

def write_changes(name, password, email):
    with open(PATH, "r") as file:
        content = json.load(file)
    id = create_id()
    content["users"][name] = {
        "password": password,
        "email": email,
        "id": id
    }
    with open(PATH, "w") as file:
        json.dump(content, file, indent=3)
    return content

def get_id(email):
    with open(PATH, "r") as file:
        content = json.load(file)
    for user in content["users"]:
        if content["users"][user]["email"] == email:
            return content["users"][user]["id"]
    return 404

@router.post('/register')
def submit_login(username: str = Form(...), password: str = Form(...), email: str = Form(...)):
    if len(password) < 8:
        error_message = "The minimum length of password is 8 characters."
        return create_new_account(error_message=error_message)
    
    if check_if_exist(username, email) == True:
        write_changes(username, password, email)
        id = get_id(email)
        return RedirectResponse(url=f"/profile/{id}", status_code=303)
    else:
        error_message = "Username or email is already occupied."
        return create_new_account(error_message=error_message)
