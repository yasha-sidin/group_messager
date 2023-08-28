import socket
import ast

class Client():

    def __init__(self, host, port):
        self._server_address = (host, port)

    def send_message(self, text):
        with socket.socket() as s:
            s.connect(self._server_address)
            s.sendall(bytes(text, encoding='UTF-8'))
            data = s.recv(1024)
        return data

    def get_data(self):
        with socket.socket() as s:
            s.connect(self._server_address)
            s.send(bytes("gvhbrtyiuvcf768f", "UTF-8"))
            result_data = str(s.recv(4096))
        return ast.literal_eval(result_data[2:len(result_data)-1])

