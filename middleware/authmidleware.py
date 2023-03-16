from flask import Request
import json
import base64

class ServerError(Exception):
    def __init__(self, *args: object, code_error = 500):
        self._error = str(*args)
        self.code_error = code_error
        super().__init__(*args)
    
    @property
    def error(self):
        return self._error, self.code_error

class MidlewareAuth:
    def __init__(self, request: Request):
        self.request = request
    
    def auth(self):
        try:
        
            hashcode = self.request.headers.get("Authorization").split(" ")
            user_data = json.loads(base64.b64decode(hashcode[1]))
            return user_data
        
        except Exception as e:
            print(f'[ERROR] => Erro de autorização => {e}')
            raise(ServerError(f'[ERROR] => Erro de autorização!', code_error = 401))