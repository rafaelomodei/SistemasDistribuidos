#!/usr/share/python
from utils.functions import FunctionUtils
from services.client import Cliente as Client
from flask import Flask, request
import json

HOST_IP = '127.0.0.1'
HOST_PORT = 14000
app = Flask("Cliente chat")
functions = FunctionUtils()


@app.route("/chat", methods=["POST"])
def sendMessage():
    try:
        mainClient = Client()
        if mainClient:
            data = json.loads(request.data)
            mainClient.sendMessage(data['message'], HOST_IP, HOST_PORT)
        return functions.message_return("Message send succeful", 200, "")
    except KeyError as e:
        return functions.message_return("", 404, "Verfiy type of parameters")
    except TypeError as e:
        return functions.message_return("", 404, "Verify type of parameters")


@app.route("/chat", methods=["GET"])
def getMessageChat():
    return "Messages"


app.run(debug=True)
