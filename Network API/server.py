import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# define the port on which to listen
port = 12345

# bind the socket to a public host, and a port
server_socket.bind((host, port))

# set the server to listen for incoming connections
server_socket.listen(5)

while True:
    # establish a connection
    client_socket, address = server_socket.accept()

    print(f"Got a connection from {address}")

    # send a message to the client
    message = "Thank you for connecting"
    client_socket.send(message.encode())

    # close the connection
    client_socket.close()