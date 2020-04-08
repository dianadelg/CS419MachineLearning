import socket

from _thread import *
import threading

print_lock = threading.Lock()


def clientMain(c):
    while True:
        try:
            data = c.recv(1024)
            if not data:
                print('Bye')
            print('Received from the client:', str(data.decode('ascii')))
            response = "I got yo message bruh"
            c.send(response.encode('ascii'))
        except:
            print('Lost connection to the client')
            return
    c.close()

def Main():
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    s.listen(12)
    print("socket is listening")

    while True:
        c, addr = s.accept()
        print('Connected to: ', addr[0], addr[1])
        start_new_thread(clientMain,(c,))
    s.close()

if __name__ == '__main__':
    Main()
