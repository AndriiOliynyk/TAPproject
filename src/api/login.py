from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
import json

router = APIRouter(tags=["login page"])
PATH = "/home/taras/Desktop/tap/tap1/demo-peremoga/TAPproject/src/credentials.json"

@router.get('/login', response_class=HTMLResponse)
def login(error_message: str = None):
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
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
            background: url('https://proedu.com/cdn/shop/articles/PRO_EDU_Photo_Courses_blog_article_titled_How_to_Get_Into_Photography-Fundamentals-20241456_x_816Photography-Fundamentals-PRO-EDU_230478f4-03a3-4add-ac0e-9b39a9524f44.jpg?v=1720542514&width=1000') no-repeat center center;
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
                {f'<p class="error-message">{error_message}</p>' if error_message else ''}
            </form>
        </div>
    </div>
</body>
</html>
"""
    return HTMLResponse(content=html_content)


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
        error_message = "The minimum length of password is 8 characters."
        return login(error_message=error_message)

    result = check_login(password, username)
    if result == "success":
        id = get_id(username)
        return RedirectResponse(url=f"/profile/{id}", status_code=303)
    else:
        error_message = "Incorrect username or password."
        return login(error_message=error_message)
