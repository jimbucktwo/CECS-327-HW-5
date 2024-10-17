import socket
UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPSocket.bind(("localhost", 1024)) #arbitrary port

valid = True
while valid:
    packetData, clientAddress = UDPSocket.recvfrom()
    UDPSocket.sendto(bytearray(str(packetData), encoding="utf-8"), clientAddress)

UDPSocket.close()