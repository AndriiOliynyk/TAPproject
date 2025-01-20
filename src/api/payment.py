from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse

app = FastAPI()

router=APIRouter()
@router.get("/payment", response_class=HTMLResponse)
async def payment_form(request: Request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Payment Form</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background: white;
                border-radius: 8px;
                padding: 20px 30px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                width: 400px;
            }
            h1 {
                text-align: center;
                color: #333;
            }
            form {
                display: flex;
                flex-direction: column;
                gap: 15px;
            }
            label {
                font-weight: bold;
                margin-bottom: 5px;
            }
            input, select, button {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                font-size: 16px;
            }
            button {
                background-color: #6c757d;
                color: white;
                font-weight: bold;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            button:hover {
                background-color: #004225;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Payment Form</h1>
            <form action="/payment" method="post">
                <label for="amount">Amount</label>
                <input type="number" step="0.01" id="amount" name="amount" required>

                <label for="currency">Currency</label>
                <select id="currency" name="currency" required>
                    <option value="USD">USD</option>
                    <option value="EUR">EUR</option>
                    <option value="UAH">UAH</option>
                </select>

                <label for="payment_method">Payment Method</label>
                <select id="payment_method" name="payment_method" required>
                    <option value="credit_card">Credit Card</option>
                    <option value="paypal">PayPal</option>
                </select>

                <label for="user_id">User ID</label>
                <input type="number" id="user_id" name="user_id" required>

                <button type="submit">Submit Payment</button>
            </form>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.post("/payment", response_class=HTMLResponse)
async def process_payment(
    amount: float = Form(...),
    currency: str = Form(...),
    payment_method: str = Form(...),
    user_id: int = Form(...),
):
    if amount <= 0:
        result = "Invalid payment amount."
    elif currency not in ["USD", "EUR", "UAH"]:
        result = "Unsupported currency."
    elif payment_method not in ["credit_card", "paypal"]:
        result = "Unsupported payment method."
    else:
        result = f"""
        <div>
            <h2>Payment Successful!</h2>
            <p>User ID: {user_id}</p>
            <p>Amount: {amount} {currency}</p>
            <p>Payment Method: {payment_method}</p>
        </div>
        """

    return HTMLResponse(content=f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Payment Status</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f4f4f9;
                margin: 0;
            }}
            .container {{
                text-align: center;
                background: white;
                border-radius: 8px;
                padding: 20px 30px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                width: 400px;
            }}
            h2 {{
                color: green;
            }}
            p {{
                font-size: 16px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {result}
        </div>
    </body>
    </html>
    """)
