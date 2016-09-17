#socket programming -
# communication server(servers info to client)-client(requesting info from server)
# websites: when you visit a website: open a socket,request info from server,
# server - port 80 open, used to transfer http data
# other websites have: ports 20,21 open- for ftp, port 22 - for ssh

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #(connection type you wanna use,what allows making a TCP connection)

print(s)

server = 'pythonprogramming.net'                           #communicate with a server

port = 80                                                  #on what port do we wanna communicate with server?

server_ip = socket.gethostbyname(server)                   #ping pythonprogrammng.net
print(server_ip)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"           #request defined as an HTTP request, where we wanted to "GET" data from the "Host" of PythonProgramming.net

s.connect((server,port))
s.send(request.encode())                                   #First we're sending the request, and encoding it
result = s.recv(4096)                                      #4096 - buffer for the resulting data, so that you receive it in manageable chunks rather than all at once
#print(result)


while(len(result) > 0):
    print(result)
    result = s.recv(4096)

