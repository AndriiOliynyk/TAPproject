from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
import json

router = APIRouter(tags=["login page"])
PATH = "/home/dmytro/tap_1/TAPproject/src/api/credentials.json"

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
            background-color: #828282;
        }
        .main-container {
            display: flex;
            width: 90%;
            max-width: 1400px;
            height: 600px;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
            background-color: #ffffff;
        }
        .left-section {
            flex: 1;
            background: url('https://i0.wp.com/digital-photography-school.com/wp-content/uploads/2024/02/how-to-become-a-good-photographer-105.jpg?resize=1500%2C1000&ssl=1') no-repeat center center;
            background-size: cover;
        }
        .right-section {
            flex: 1;
            padding: 60px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            text-align: center;
        }
        .right-section h1 {
            font-size: 32px;
            color: #333;
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            font-size: 18px;
            color: #555;
            display: block;
            margin-bottom: 8px;
        }
        input {
            width: 100%;
            padding: 12px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        button {
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
        }
        button:hover {
            background-color: #004225;
        }
    </style>
</head>
<body>
    <div class="main-container">
        <div class="left-section"></div>
        <div class="right-section">
            <h1>Welcome</h1>
            <form action="/submit-login" method="post">
                <div class="form-group">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>
                </div>
                <div class="form-group">
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
    </div>
</body>
</html>
"""
    return html_content

def check_login(password, login):
    with open(PATH, "r") as file:
        content = json.load(file)
    try:
        for user in content["users"]:
            if str(login) == str(user):
                if str(content["users"][user]["password"]) == str(password):
                    return "success"
                else:
                        return "wrong pas3sword or login"
            if str(content["users"][user]["email"]) == str(login):
                if str(content["users"][user]["password"]) == str(password):
                    return "success"
                else:
                    return "wrong pass4word or login"
    except Exception as e:
        return e
        # for user in content["users"]:
        #     if content["users"][user]["email"] == login:
        #         if str(password) != str(content["users"][str(login)]["password"]):
        #             return "wrong password or login"
        #     if str(user) == (login):
        #         if str(password) != str(content["users"][user]["password"]):
        #             return "wrong password or login"
        #         login = user
            # else:
            #     return "success"


def get_id(login):
    with open(PATH, "r") as file:
        content = json.load(file)
    for user in content["users"]:
        if str(user) == str(login):
            id = content["users"][user]["id"]
            return id
        if str(content["users"][user]["email"]) == str(login):
            id = content["users"][user]["id"]
            return id

@router.post('/submit-login')
def submit_login(username: str = Form(...), password: str = Form(...)):
    if len(password) < 8:
        return "the minimum length of password is 8 characters"

    if check_login(password, username) == "success":
        id = get_id(username)
        return RedirectResponse(url=f"/profile/{id}", status_code=303)
    else:
        return "end"