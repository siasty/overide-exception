import requests

class SymfoniaHTTPError(Exception):
    response = None  

    def __init__(self, message):
        self.message = message
        super().__init__(message)

class SymfoniaResponse(requests.Response):
    def raise_for_status(self):
        http_error_msg = ''
        if 400 <= self.status_code < 500:
            http_error_msg = f'{self.status_code} Client Error: {self.reason}'
        elif 500 <= self.status_code < 600:
            http_error_msg = f'{self.status_code} Server Error: {self.reason}'
        if http_error_msg:
            SymfoniaHTTPError.response = self  
            raise SymfoniaHTTPError(http_error_msg)


def symfonia_request(method, url, **kwargs):
    response = requests.request(method, url, **kwargs)
    response.__class__ = SymfoniaResponse
    return response