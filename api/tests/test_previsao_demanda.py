
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_previsao_demanda():
    response = client.get("/previsao_demanda/")
    assert response.status_code == 200
    assert response.json() == {"message": "Previsão de Demanda"}
