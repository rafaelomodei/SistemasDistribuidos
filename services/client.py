import socket


class Cliente:
    def __init__(self):
        self.connect = socket.socket()

    def sendMessage(self, message, address_connect, port_connect):
        self.connect.connect((address_connect, port_connect))
        # host_ip = bytearray(address_connect, "ascii")
        self.connect.send(message.encode())
        data = self.connect.recv(1024).decode()
        print(data)
        message = "Digite a sua mensagem"

        self.connect.close()
