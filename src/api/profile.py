ґfrom fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["login page"])

@router.get('/profile/{user_id}', response_class=HTMLResponse)
def profile(user_id: int):
    user = users_data.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="profile not found")

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{user['name']}'s Profile</title>
        <style>
            /* ваш css код */
        </style>
    </head>
    <body>
        <div class="container">
            <div class="left-panel">
                <div class="profile-pic" style="background-image: url('{user['profile_image']}');">
                    <div class="profile-options">
                        <button onclick="changePhoto()">Change Photo</button>
                        <button onclick="deletePhoto()">Delete Photo</button>
                    </div>
                </div>
                <h3>Favorite Photos</h3>
                <!-- Додайте улюблені фото динамічно -->
            </div>
            <div class="right-panel">
                <div class="field">
                    <label for="name">Full Name:</label>
                    <input type="text" id="name" value="{user['name']}" readonly>
                </div>
                <div class="field">
                    <label for="rental-minutes">Rental Minutes:</label>
                    <input type="text" id="rental-minutes" value="{user['rental_minutes']}" readonly>
                </div>
                <div class="field">
                    <label for="favorite-place">Favorite Place:</label>
                    <input type="text" id="favorite-place" value="{user['favorite_place']}" readonly>
                </div>
            </div>
        </div>
        <script>
            function changePhoto() {
                alert("change photo clicked!");
            }
            function deletePhoto() {
                alert("delete photo clicked!");
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
