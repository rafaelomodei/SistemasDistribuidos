import socket


class Server:
    HOST_CONNECT = "127.0.0.1"
    SIZE_MSG = 103400

    def __init__(self, address_host, port_host):
        self.connect = socket.socket()
        self.connect.bind((address_host, port_host))
        self.connect.listen(2)

    def listenMessage(self):
        conn, address = self.connect.accept()
        dataMsa = conn.recv(self.SIZE_MSG).decode()

        print("from connected user: " + str(dataMsa), address[0])
        data = "ok"
        conn.send(data.encode())
        conn.close()
