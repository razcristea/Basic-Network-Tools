import socket

host = 'localhost'
port = 54321

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

print('Server started on {}, listening on TCP port {}'.format(host, port))

conn, addr = s.accept()

print('Incoming connection from {}:{}...'.format(addr[0], addr[1]))

while True:
    data = conn.recv(1024)
    if not data:
        break
    print('Received following data: {}'.format(data.decode('utf-8')))
    conn.sendall(data)

print('Server is shutting down. Bye!')
conn.close()
