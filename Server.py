from flask import Flask
from flask import abort, request, jsonify, make_response, json
from functools import wraps
import json
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
#la linea inferior de codigo tiene el proposito de permitir saltar los protocolos CORS y realizar pruebas con una pagina en Node JS
cors = CORS(app, resources = {r"/*": {"origins" : "*"}})




#funcion devuelve toda la informacion publica de la red de cargadores en el mapa
@app.route('/getNetwork', methods = ['GET'])
def getNetwork():
    global chargers
    try:
        data = makeJsonList(chargers)
        response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
        return response
    except:
        return abort(400, "Unable to process request")

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)