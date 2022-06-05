import requests

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok",
            "errors": [],
            "message": "I'm alive."}


@app.get("/api/v1/london")
def london_weather():
    try:
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=c86317f2ceea13d26d9ed80fc5c08c91")
    except Exception as e:
        return {"status": "error",
                "errors": [f"Could not read data from the API: {e}"],
                "message": None}

    if response.status_code == 200:
        return {"status": "ok",
                "errors": [],
                "message": response.json()}
    else:
        return {"status": "error",
                "errors": [f"Could not read data from the API: {response.status_code} {response.reason}."],
                "message": None}
