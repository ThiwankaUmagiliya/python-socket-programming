import socket

host = '127.0.0.1' # Standard loopback interface address
port = 54321 # Define the port on which you want to connect

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server on local computer
client.connect((host, port))


# Get value from Server
from_server = client.recv(4096)

# Print the value received from Server
print("Received from Server: ", str(from_server, 'utf-8'))

client.close()
print("All are Okay - Connection Terminated !")
