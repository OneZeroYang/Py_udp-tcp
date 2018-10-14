import socket
UDP=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
   o=input("请输入内容")
   id=("127.0.0.1",8080)
   if o=="exit":
       break
   UDP.sendto(o.encode("utf-8"),("192.168.1.5", 8080))
UDP.close()




