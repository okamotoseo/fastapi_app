import os

class Config:
    DATABASE_URL = os.getenv('DATABASE_URL', "sqlite:///./test.db")
    GOOGLE_CLOUD_PROJECT = os.getenv('GOOGLE_CLOUD_PROJECT', "cool-benefit-267222")
    GOOGLE_CLOUD_LOCATION = os.getenv('GOOGLE_CLOUD_LOCATION', "us-central1")
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', "/home/willians_seo/.config/gcloud/application_default_credentials.json")
    VERTEX_AI_CREDENTIALS = os.getenv('VERTEX_AI_CREDENTIALS', "/home/willians_seo/.config/gcloud/application_default_credentials.json")

config = Config()

