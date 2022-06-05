------
This is the weather_app sample app's documentation
------

To run the app simply go to the app's root directory and run it with docke compose

    docker-compose up -d weather_app

Then the app is available on the localhost. Open the following URL in your browser for the available API

    localhost:8080/docs

Two endpoints available:

    / - for the aliveness status
    localhost:8080/api/v1/london - for the weather in London.

API returns a json object to be used by a client (a mobile or a web app)

In case there's no docker installed on your environment, the app could be started this way:

1. Go to the app root dir
2. run "pipenv install" to run a new virtual env and install the required packages
3. run "pipenv run uvicorn src.main:app"
4. The weather_app is available on your localhost at http://0.0.0.0:8080

-------
Tests
-------

Tests could be run with docker as well. To run tests simply:

    docker-compose up weather_app_pytest
