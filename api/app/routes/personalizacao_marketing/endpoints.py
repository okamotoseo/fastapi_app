from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_personalizacao_marketing():
    return {"message": "Personalização de Marketing"}

