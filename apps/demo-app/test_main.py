from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert data["application"] == "CloudPulse Demo Application"
    assert data["version"] == "1.0.0"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data


def test_api_info():
    response = client.get("/api/info")
    assert response.status_code == 200

    data = response.json()
    assert data["application"] == "cloudpulse-demo-app"
    assert data["managed_by"] == "CloudPulse"
