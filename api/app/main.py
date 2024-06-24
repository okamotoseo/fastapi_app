import sys
import os

# Adicione o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

# Adicione o diretório 'app' ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/')

from fastapi import FastAPI
from app.routes.vertex_ai.vertex_ai_routes import router as vertex_ai_router
from app.middleware import CustomMiddleware  # Importar o middleware
from app.routes.dialogflow_webhook.endpoints import router as dialogflow_webhook_router
app = FastAPI()

# Adicionar o middleware ao aplicativo
app.add_middleware(CustomMiddleware)
app.include_router(vertex_ai_router, prefix="/api/v1", tags=["Vertex AI"])
app.include_router(dialogflow_webhook_router, prefix="/dialogflow", tags=["Dialogflow"])
@app.get("/")
async def root():
    return {"message": "API FastAPI com estrutura modular"}

