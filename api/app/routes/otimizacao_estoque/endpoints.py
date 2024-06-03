from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_otimizacao_estoque():
    return {"message": "Otimização de Estoque"}

