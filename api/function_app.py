import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="message")
def message(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        message = {
            "text": f"Hello, {name}. This HTTP triggered function executed successfully."
        }
        return func.HttpResponse(json.dumps(message))
    else:
        message = {
            "text": "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response."
        }
        return func.HttpResponse(
             json.dumps(message),
             status_code=200
        )

@app.route(route="log", auth_level=func.AuthLevel.FUNCTION)

def log(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This is log API.")
    else:
        return func.HttpResponse(
             "This  is log API. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )