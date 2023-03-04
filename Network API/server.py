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

print(f"Server listening on {host}:{port}")

while True:
    # establish a connection
    client_socket, address = server_socket.accept()

    print(f"Got a connection from {address}")

    # receive the filename from the client
    filename = client_socket.recv(1024).decode()

    # open the file and read the contents
    with open(filename, "rb") as file:
        file_data = file.read()

    # send the file contents to the client
    client_socket.sendall(file_data)

    # close the connection
    client_socket.close()