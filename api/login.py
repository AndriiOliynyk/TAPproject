from fastapi import APIRouter

router = APIRouter(tags="login page")

@router.get('/login')
def login():
    return "success"
#sadas
