import os
from fastapi import APIRouter, HTTPException, Request, Body
from fastapi.responses import JSONResponse
from app.services.vertex_ai.vertex_ai_service import VertexAIService
from app.models.vertex_ai.vertex_ai_models import VertexAIRequest, VertexAIResponse
import logging

router = APIRouter()

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/generate-description-json", response_model=VertexAIResponse)
async def generate_description_json(
    request: Request,
    json_body: VertexAIRequest = Body(..., media_type="application/json")
):
    google_creds = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not google_creds:
        raise HTTPException(status_code=500, detail="GOOGLE_APPLICATION_CREDENTIALS not set")
    else:
        logger.info(f"GOOGLE_APPLICATION_CREDENTIALS: {google_creds}")

    try:
        service = VertexAIService()
    except Exception as e:
        logger.error(f"Erro ao instanciar VertexAIService: {e}")
        raise HTTPException(status_code=500, detail="Erro ao inicializar o serviço VertexAI")

    try:
        body_content = json_body.input_code
        logger.info(f"Conteúdo recebido: {body_content}")
        request_data = VertexAIRequest(input_code=body_content)
        response_data = service.generate_description(request_data)
        return response_data
    except Exception as e:
        logger.error(f"Erro durante o processamento: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate-description-text", response_model=VertexAIResponse)
async def generate_description_text(
    request: Request,
    text_body: str = Body(..., media_type="text/plain")
):
    google_creds = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not google_creds:
        raise HTTPException(status_code=500, detail="GOOGLE_APPLICATION_CREDENTIALS not set")
    else:
        logger.info(f"GOOGLE_APPLICATION_CREDENTIALS: {google_creds}")

    try:
        service = VertexAIService()
    except Exception as e:
        logger.error(f"Erro ao instanciar VertexAIService: {e}")
        raise HTTPException(status_code=500, detail="Erro ao inicializar o serviço VertexAI")

    try:
        body_content = text_body
        logger.info(f"Conteúdo recebido: {body_content}")
        request_data = VertexAIRequest(input_code=body_content)
        response_data = service.generate_description(request_data)
        return response_data
    except Exception as e:
        logger.error(f"Erro durante o processamento: {e}")
        raise HTTPException(status_code=500, detail=str(e))

