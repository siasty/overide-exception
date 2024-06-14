import excp
import requests
import json
from excp import symfonia_request, SymfoniaHTTPError

try:
    url = "https://dummy.restapiexample.com/api/v1/create"

    payload = json.dumps({
        "name": "test",
        "salary": "123",
        "age": "23"
    })
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }

    response = symfonia_request("POST", url, headers=headers, data=payload)
    response.raise_for_status()

except SymfoniaHTTPError as e:
    print(e)
