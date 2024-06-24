from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            logger.info(f"Processando requisição: {request.method} {request.url}")
            response = await call_next(request)
        except Exception as e:
            logger.error(f"Erro durante o processamento da requisição: {e}")
            response = Response("Internal server error", status_code=500)
        finally:
            logger.info(f"Resposta gerada: {response.status_code}")
        return response

