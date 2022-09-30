from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
def read_root():
    """Ping the API."""
    message = "LHK"
    return {"ping": f"pong from {message}!"}
