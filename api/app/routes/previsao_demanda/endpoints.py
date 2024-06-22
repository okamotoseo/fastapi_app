from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_previsao_demanda():
    return {"message": "Previsão de Demanda"}

