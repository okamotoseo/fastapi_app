from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_recomendacoes_produtos():
    return {"message": "Recomendações de Produtos"}

