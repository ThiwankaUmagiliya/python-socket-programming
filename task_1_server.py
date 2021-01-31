import socket


host = '127.0.0.1' # Standard loopback interface address
port1 = 12345 # Define the port on which you want to connect Client 1
port2 = 54321 # Define the port on which you want to connect Client 2

serv1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv1.bind((host, port1)) # Connect to client1 on local computer
serv2.bind((host, port2)) # Connect to client1 on local computer

serv1.listen(5)
serv2.listen(5)


conn1, addr = serv1.accept()
conn2, addr = serv2.accept()

# Get value from Client 1
data = conn1.recv(4096)

# Increase the ASCII value of the received data
sentdata = chr(ord(data) + 1)
print("Received: ", str(data, 'utf-8'))

# Sending the value to Client 2
conn2.send(str.encode(sentdata))
print("Sent    : ", sentdata)

conn1.close()
conn2.close()
print("All are Okay - Connection Terminated !")




