import json
import os

from flask import Flask, request

HOST = '0.0.0.0' if os.getenv('HOSTNAME') == 'api' else '127.0.0.1'
app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to the api"


@app.route('/conveyor', methods=["POST"])
def conveyor():
    task = json.loads(request.data)
    return task


app.run(host=HOST, port=9999, debug=True)
