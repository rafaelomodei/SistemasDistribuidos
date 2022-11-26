#!/usr/share/python
from services.server import Server


def mainServer():
    mainServer = Server('127.0.0.1', 14000)

    if mainServer:
        mainServer.listenMessage()


try:
    mainServer()
except TypeError as e:
    print(e)
    print("Verifique os parâmetros de conexão")
except KeyboardInterrupt:
    print("\nTchau")
