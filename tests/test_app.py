import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Deployed by GitHub Actions" in response.data


def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_greet_with_name(client):
    response = client.get("/api/greet?name=Prashant")
    assert response.get_json()["message"] == "Hello, Prashant!"


def test_greet_without_name_is_rejected(client):
    response = client.get("/api/greet")
    assert response.status_code == 400


def test_add_two_numbers(client):
    response = client.get("/api/add?a=2&b=3")
    assert response.get_json()["result"] == 5
