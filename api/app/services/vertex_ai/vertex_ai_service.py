import os
import json
import requests
import logging
from app.models.vertex_ai.vertex_ai_models import VertexAIRequest, VertexAIResponse
from app.config import config

class VertexAIService:

    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.VERTEX_AI_CREDENTIALS
        self.api_endpoint = "us-central1-aiplatform.googleapis.com"
        self.project_id = config.GOOGLE_CLOUD_PROJECT
        self.location_id = config.GOOGLE_CLOUD_LOCATION
        self.model_id = "gemini-1.5-pro-001"

        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    def get_access_token(self):
        command = "gcloud auth print-access-token"
        access_token = os.popen(command).read().strip()
        self.logger.debug(f"Access Token: {access_token}")
        return access_token

    def generate_description(self, request: VertexAIRequest) -> VertexAIResponse:
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": f"Analyze the following code and generate a detailed description:\n{request.input_code}"
                        },
                    ]
                }
            ],
            "generationConfig": {
                "maxOutputTokens": 256,
                "stopSequences": ["\\n\\n"],
                "temperature": 0.7,
                "topP": 0.95,
            },
            "safetySettings": [
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                }
            ],
        }

        self.logger.debug(f"Request Payload: {json.dumps(payload, indent=2)}")

        url = f"https://{self.api_endpoint}/v1/projects/{self.project_id}/locations/{self.location_id}/publishers/google/models/{self.model_id}:streamGenerateContent"

        response = requests.post(url, headers=headers, json=payload)

        self.logger.debug(f"Response Status Code: {response.status_code}")
        self.logger.debug(f"Response Text: {response.text}")

        if response.status_code == 200:
            result = response.json()
            self.logger.debug(f"Response JSON: {json.dumps(result, indent=2)}")
            if isinstance(result, list) and len(result) > 0:
                description_parts = [candidate['content']['parts'][0]['text'] for response in result for candidate in response['candidates']]
                description = " ".join(description_parts)
                return VertexAIResponse(description=description)
            else:
                raise ValueError(f"Unexpected response format: {json.dumps(result, indent=2)}")
        else:
            response.raise_for_status()

