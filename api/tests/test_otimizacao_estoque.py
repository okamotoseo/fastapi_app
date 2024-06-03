from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_otimizacao_estoque():
    response = client.get("/otimizacao_estoque/")
    assert response.status_code == 200
    assert response.json() == {"message": "Otimização de Estoque"}

