import socket

HOST = '192.168.149.25'
PORT = 49671

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

data = 'Hello world'
s.send(data.encode('utf-8'))
print('Send[1]: ', data)

data = s.recv(1024)
s.close()

print('Received[4]: ', data)
