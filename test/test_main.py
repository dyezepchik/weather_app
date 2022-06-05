from unittest import mock

from fastapi.testclient import TestClient
from requests import Response

from src.main import app

client = TestClient(app)

SUCCESS_RESPONSE_STUB = b'{"status":"ok","errors":[],"message":{"coord":{"lon":-0.1257,"lat":51.5085},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"base":"stations","main":{"temp":287.94,"feels_like":287.69,"temp_min":286.4,"temp_max":289.21,"pressure":1016,"humidity":85},"visibility":10000,"wind":{"speed":2.06,"deg":280},"clouds":{"all":100},"dt":1654445294,"sys":{"type":2,"id":2019646,"country":"GB","sunrise":1654400787,"sunset":1654459909},"timezone":3600,"id":2643743,"name":"London","cod":200}}'
UNAUTHORIZED_RESPONSE_STUB = b'{"status":"error","errors":["Could not read data from the API: 401 Unauthorized."],"message":null}'
NOT_FOUND_RESPONSE_STUB = b'{"status":"error","errors":["Could not read data from the API: 404 Not Found."],"message":null}'


def test_get_root():
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "errors" in data
    assert data["errors"] == []
    assert "message" in data


def test_get_london_weather_positive():
    with mock.patch("src.main.requests.get") as mocked_request:
        resp = Response()
        resp.status_code = 200
        resp.reason = "Ok"
        resp._content = SUCCESS_RESPONSE_STUB
        # resp._content_consumed = True
        mocked_request.return_value = resp

        resp = client.get("/api/v1/london")

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "errors" in data
    assert data["errors"] == []
    assert "message" in data


def test_get_london_weather_error():
    with mock.patch("src.main.requests.get") as mocked_request:
        resp = Response()
        resp.status_code = 401
        resp.reason = "Unauthorized"
        resp._content = UNAUTHORIZED_RESPONSE_STUB
        mocked_request.return_value = resp

        resp = client.get("/api/v1/london")

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "error"
    assert "errors" in data
    assert len(data["errors"]) == 1
    assert data["errors"][0] == "Could not read data from the API: 401 Unauthorized."
