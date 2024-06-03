from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_segmentacao_clientes():
    return {"message": "Segmentação de Clientes"}

