import pytest  # type: ignore[import-not-found]
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_greet_returns_message_for_name(client):
    response = client.get("/api/greet?name=Yogesh")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello, Yogesh!"


def test_greet_without_name_returns_400(client):
    response = client.get("/api/greet")
    assert response.status_code == 400
    assert response.get_json()["error"] == "name is required"


def test_add_returns_sum_of_integers(client):
    response = client.get("/api/add?a=2&b=3")
    assert response.status_code == 200
    assert response.get_json()["result"] == 5


def test_add_with_non_integer_returns_400(client):
    response = client.get("/api/add?a=abc&b=3")
    assert response.status_code == 400
    assert response.get_json()["error"] == "a and b must be integers"