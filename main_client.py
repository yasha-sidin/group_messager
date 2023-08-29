from Client.Client import Client
from Server.Client_frame import Client_frame

if __name__ == '__main__':
    client = Client('localhost', 8888)
    frame = Client_frame(client)
    frame.initialize()