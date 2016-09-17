#client-server,sending & receiving data using sockets
#create a simple server system that accepts incoming connections and some data we type
#server-needs to be able to accept data & send back data specifically to the connection in question

import socket
import sys
from _thread import*

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)                                                        #a queue-how many incoming connenctions will fit
print('Waiting for the connection')

def threaded_client(conn):
    conn.send(str.encode('Welcome,typeyour info\n'))

    while True:
        data = conn.recv(2048)
        reply = 'Server output: '+ data.decode('utf-8')         #decode all the data received
        if not data:
            break                                               #stop connection if no data received
        conn.sendall(str.encode(reply))                         #encode the reply,send it back
    conn.close()

while True:
    conn, addr = s.accept()
    print('connected to:' + addr[0] + ':' + str(addr[1]))

    start_new_thread(threaded_client,(conn,))

# cmd:
# telnet
# ipconfig -> find the local ip address
# telnet 192.168.17.1 5555


