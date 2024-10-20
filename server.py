import socket
import random

# socket created
TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#gets the IP address of the server
hostname = socket.gethostname()
IPaddress = socket.gethostbyname(hostname)

# assigns a random port number
port = random.randint(1024, 49151)

#binds the IP and port to the socket and listens to the client
TCPSocket.bind((IPaddress, port)) 
TCPSocket.listen(5)
print(f"IP address of server : {IPaddress}\nPort Number : {port}\nServer listening...")

incomingSocket, incomingAdress = TCPSocket.accept()

# infinite loop to listen to the client and send data back until the client closes the connection
while True:
    myData = incomingSocket.recv(1024).decode()
    if myData:
        print(f'Received "{myData}" from the client')
        incomingSocket.sendall(myData.upper().encode())
    else:
        print("Done")
        break

incomingSocket.close()
