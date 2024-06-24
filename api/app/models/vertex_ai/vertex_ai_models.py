from pydantic import BaseModel

class VertexAIRequest(BaseModel):
    input_code: str

class VertexAIResponse(BaseModel):
    description: str

