from fastapi import APIRouter

auth_router = APIRouter()


@auth_router.get("/")
async def auth():
    return {"login": "processing 534"}
