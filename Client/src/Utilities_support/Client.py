import socket
import sys
import os
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])

def remote_command(data, Appium_IP):
    host = Appium_IP
    port = 9999
    s = socket.socket()
    s.connect((host, port))
    if len(data) > 0:
        print(data)
        s.send(data.encode("utf-8"))
        recv_data = s.recv(1024)
        s.close()
        return recv_data.decode("utf-8")

#print(remote_command('netstat -ano | find "4724"'))
