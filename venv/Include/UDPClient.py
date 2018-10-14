import socket

UDPClient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
locad=("",8081)
UDPClient.bind(locad)
while True:
 s=UDPClient.recvfrom(1024)

 neirong=s[0]
 add=s[1]
 print("%s:%s" % (str(add),neirong.decode("utf_8")))



UDPClient.close()