import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "10.20.205.221"

# define the port on which to connect
port = 12345

# connect to the server
client_socket.connect((host, port))

# send the filename to the server
filename = "example.jpg"
client_socket.send(filename.encode())

# receive the file contents from the server
file_data = b""
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    file_data += data

# write the file contents to a file
with open(filename, "wb") as file:
    file.write(file_data)

# close the connection
client_socket.close()
