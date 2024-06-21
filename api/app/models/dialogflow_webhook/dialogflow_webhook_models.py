from pydantic import BaseModel
from typing import Any, Dict, List, Optional

class Text(BaseModel):
    text: List[str]

class FulfillmentMessage(BaseModel):
    text: Text

class OutputContext(BaseModel):
    name: str
    lifespanCount: int
    parameters: Dict[str, Any]

class Intent(BaseModel):
    name: Optional[str]
    displayName: str

class QueryResult(BaseModel):
    queryText: str
    parameters: Dict[str, Any]
    allRequiredParamsPresent: bool
    fulfillmentText: str
    fulfillmentMessages: List[FulfillmentMessage]
    outputContexts: List[OutputContext]
    intent: Intent
    intentDetectionConfidence: float
    languageCode: str

class OriginalDetectIntentRequest(BaseModel):
    payload: Dict[str, Any]

class WebhookRequest(BaseModel):
    responseId: str
    queryResult: QueryResult
    originalDetectIntentRequest: OriginalDetectIntentRequest
    session: str

