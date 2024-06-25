from fastapi.testclient import TestClient


def test_read_data(client: TestClient):
    response = client.get("/v1/iris")
    assert response.status_code == 200
    assert len(response.json()) > 0
