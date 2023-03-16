from flask import Flask, request, jsonify 
from middleware.authmidleware import MidlewareAuth, ServerError

import os

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "Server": "Server_name",
        "Version": "1.0.0",
        "type": os.environ.get("FLASK_ENV") or "production"
    })
    
@app.route("/listvalues")
def listvalues():
    try:
        user = MidlewareAuth(request).auth()
        if user.get("idUsuario") == "1":
            return jsonify([1,2,3,4,5])
        else:
            raise(ServerError("Usuário sem permissão!", code_error=401))
    except ServerError as e:
        return e.error

if __name__ == '__main__':
    app.run(debug=True, port="5500")