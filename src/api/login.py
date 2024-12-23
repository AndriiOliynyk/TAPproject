from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
import json

router = APIRouter(tags=["login page"])

@router.get('/login', response_class=HTMLResponse)
def login():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login Page</title>
    </head>
    <body>
        <h1>Login</h1>
        <form action="/submit-login" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <br><br>
            <button type="submit">підтвердити</button>
        </form>
    </body>
    </html>
    """
    return html_content


def check_login(password, login):
    with open("/home/dmytro/tap_1/TAPproject/src/api/credentials.json", "r") as file:
        content = json.load(file)
    try:
        if str(password) != str(content["users"][str(login)]["password"]):
     
            return "wrong password or login"
        else:
            return "success"
    except KeyError:
        return "wrong password or login"

@router.post('/submit-login')
def submit_login(username: str = Form(...), password: str = Form(...)):
    return check_login(password, username)
    


    
