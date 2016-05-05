import socket

host = 'localhost'
port = 54321
data_out = b'Hello World!'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print('Connected to server: {} on port {}'.format(host, port))
print('Sending some data...')
s.sendall(data_out)

data_in = s.recv(1024)
print('Response from server: {}'.format(data_in.decode('utf-8')))

s.close()
print('Connection closed.')
