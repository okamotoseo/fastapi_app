from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_analise_preditiva():
    return {"message": "Análise Preditiva"}

