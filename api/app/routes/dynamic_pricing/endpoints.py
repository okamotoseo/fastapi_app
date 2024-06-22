from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_dynamic_pricing():
    return {"message": "Dynamic Pricing"}

