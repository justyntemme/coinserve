import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost' 
port = 8888
sock.connect((host,port))
message = "-a btce 1 btc usd"
sock.sendall(message.encode())
data = sock.recv(1024).decode()
print (data)
sock.close()
