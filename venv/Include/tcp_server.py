import socket

tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server.bind(('',8081))
while True:
 tcp_server.listen(128)
 client_socket,client_ip=tcp_server.accept()
 print(client_ip)
 # idd= listen(client_socket)
 while True:
  data=client_socket.recv(1024)
  print(data.decode("utf-8"))
  client_socket.send("收到您的消息".encode("utf-8"))

 def listen(client_socket):
     # while True:
       data = client_socket.recv(1024)
       print(data.decode("utf-8"))
       client_socket.send("收到您的消息".encode("utf-8"))




