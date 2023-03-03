import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# define the port on which to connect
port = 12345

# connect to the server
client_socket.connect((host, port))

# receive data from the server
data = client_socket.recv(1024)

# decode the received data
message = data.decode()

# print the received message
print(f"Received message: {message}")

# close the connection
client_socket.close()