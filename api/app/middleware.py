from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info(f"Processando requisição: {request.url}")
        response = await call_next(request)
        logger.info(f"Resposta gerada: {response.status_code}")
        return response

