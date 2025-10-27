from fastapi import APIRouter


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def auth_test():
    return "auth test"

from pydantic import BaseModel

class RegisterRequest(BaseModel):
    username: str 
    password: str

@router.post("/register")
async def register(register_request: RegisterRequest):
    pass

@router.post("/login")
async def login():
    pass
