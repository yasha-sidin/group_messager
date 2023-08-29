import socket
import threading
from time import sleep


class Server:

    def __init__(self, host, port):
        self._server_address = (host, port)
        self._messages_queue = []

    def start_server(self):
        with socket.socket() as s:
            s.bind(self._server_address)
            s.listen(100)
            while True:
                conn, address = s.accept()
                result_data = str(conn.recv(4096))

                if result_data[2:len(result_data)-1] == "gvhbrtyiuvcf768f":
                    conn.send(bytes(str(self._messages_queue), "UTF-8"))
                else:
                    self._messages_queue.append(result_data)
                    conn.send(bytes("received", "UTF-8"))

