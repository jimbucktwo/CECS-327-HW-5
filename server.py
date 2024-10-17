import socket


TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPSocket.bind(('localhost', 1024)) 
TCPSocket.listen(5)
print("Server listening...")

incomingSocket, incomingAdress = TCPSocket.accept()

while True:
    myData = incomingSocket.recv(1024).decode()
    if myData:
        print(f'Received "{myData}" from the client')
        incomingSocket.sendall(myData.upper().encode())
    else:
        print("Done")
        break

incomingSocket.close()