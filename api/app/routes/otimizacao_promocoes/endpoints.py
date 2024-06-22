from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_otimizacao_promocoes():
    return {"message": "Otimização de Promoções"}

