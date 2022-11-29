### Readme
This repo demonstrates how to create unit tests for a basic Flask app - using the `pytest` module.
The unit tests can run on webpages that your web app returns, as well as responses from Api endpoints. This web app is running on port 80, so after you run the code, you can view it by going to `http://localhost` or `http://localhost:80` - they are the same. 

This project has one route for home that returns some html and an API endpoint. Depending on if the HTTP request is a GET or POST, the responses will differ. The path of the API endpoint is `/api/DemoApiEndpoint`. When a POST request is sent, the endpoint expects a JSON body with a `name` field of type string.

### Tests
Run the command: `python3 -m pytest` or `python -m pytest`
This will invoke pytest which will execute all the python files prefixed with the name `test_` - which are located within the `tests` dir of this project. 