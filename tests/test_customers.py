from fastapi.testclient import TestClient
from Test7 import app


client = TestClient(app)


def test_get_customers_status():
    response = client.get("/customers")
    assert response.status_code == 200


def test_get_customers_content():
    response = client.get("/customers")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    first = data[0]
    assert "id" in first
    assert "name" in first
