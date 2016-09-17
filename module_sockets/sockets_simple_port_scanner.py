# port scanner - scans ports & tells if port is open/closed

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'pythonprogramming.net'

def pscan(port):                    #scans ports to check if they're open
    try:
        s.connect((server,port))
        return  True                #if we can connect
    except:
        return False


for x in range(1,26):                #tests port1->port26
    if pscan(x):
        print('Port', x, 'is open')
    else:
        print('Port', x, 'is closed')
