from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_deteccao_fraudes():
    return {"message": "Detecção de Fraudes"}

