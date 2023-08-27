from Client.Client import Client

Client('localhost', 8888).send_message("text")
print(Client('localhost', 8888).get_data())
