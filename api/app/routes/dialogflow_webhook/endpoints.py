from fastapi import APIRouter, Request, HTTPException
from google.cloud import dialogflow

import os
import logging
import time
from app.models.dialogflow_webhook.dialogflow_webhook_models import WebhookRequest

router = APIRouter()

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carregar credenciais do Dialogflow
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/var/www/fastapi_app/dialogflow-credentials.json"

@router.post("/webhook")
async def webhook(request: Request):
    start_time = time.time()
    try:
        request_data = await request.json()
        logger.info("Recebendo solicitação: %s", request_data)
        
        # Validar o corpo da requisição usando Pydantic
        webhook_request = WebhookRequest(**request_data)

        fulfillment_text = webhook_request.queryResult.fulfillmentText
        if fulfillment_text:
            logger.info("Resposta do Dialogflow: %s", fulfillment_text)
            return {"fulfillmentText": fulfillment_text}
        else:
            logger.warning("Nenhum texto de resposta do Dialogflow encontrado")
            fallback_text = f"Sorry, I couldn't understand your request about '{webhook_request.queryResult.queryText}'. Can you rephrase?"
            return {"fulfillmentText": fallback_text}
    except Exception as e:
        logger.error("Erro ao processar a solicitação: %s", e)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        end_time = time.time()
        processing_time = end_time - start_time
        logger.info("Tempo de processamento: %s segundos", processing_time)

def detect_intent_texts(project_id, session_id, text, language_code):
    try:
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(project_id, session_id)
        logger.info("Session Path: %s", session)

        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        logger.info("Detect Intent Response: %s", response)

        return response
    except Exception as e:
        logger.error("Erro ao detectar intenção: %s", e)
        raise

