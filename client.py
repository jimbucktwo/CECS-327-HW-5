import socket

# creates a socket
TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# prompts the user to enter an IP address and port number, keeps trying until it successfully connects
while True:
    try:
        serverIP = str(input("Enter IP address: "))
        serverPort = int(input("Enter port number: "))
        TCPSocket.connect((serverIP, serverPort))
        break
    except:
        print("Either the IP address or port number was entered incorrectly, try again.")


# infinite loop so the user can send as many messages as they want
while True:
    message = input("Enter message you want to send (Enter to exit): ")
    if message:
        # sends the message to the server
        TCPSocket.sendall(message.encode())
        serverResponse = TCPSocket.recv(1024)
        print(f'Server Response: "{serverResponse.decode()}"')
    else:
        break

#closes the socket
TCPSocket.close()
