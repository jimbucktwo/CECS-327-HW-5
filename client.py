import socket

UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

valid = True
while valid:
    myMessage = input("Enter message that you want to send: ")
    UDPSocket.sendto(bytearray(str(myMessage), encoding="utf-8"), ('serverIP', 'UDPPort')) # create these variables later

UDPSocket.close()