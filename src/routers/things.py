from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_index():
    return {
        "magic": 500,
        "message": "Lorem ipsum, eigh?",
    }
