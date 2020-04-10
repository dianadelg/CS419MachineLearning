import socket
import tqdm
from _thread import *
import threading

print_lock = threading.Lock()

BUFFER_SIZE = 4096 # send 4096 bytes each time step

def clientMain(c):
    while True:
        try:
            data = c.recv(16)
            message = str(data.decode('ascii'))
            if not message:
                print('Bye')
            print('Received from the client:', message)
            if message.lower().strip() == "submission":
                data = c.recv(1024)
                filename = str(data.decode('ascii')).split()[0]
                filesize = str(data.decode('ascii')).split()[1]
                filesize = int(filesize)
                storeSubmission(c,filesize,filename)
            response = "I got yo message bruh"
            c.send(response.encode('ascii'))
        except:
            print('Lost connection to the client')
            return
    c.close()
def storeSubmission(c, fs, fn):
    ready = "ready"
    c.send(ready.encode('ascii'))
    with open(fn, "wb") as f:
        total = 0
        while (total <= fs):
            bytes_read = c.recv(BUFFER_SIZE)
            if total <= fs:
                f.write(bytes_read)
            total += BUFFER_SIZE
        f.close()


def Main():
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
    s.listen(12)
    print("socket is listening")
    while True:
        client, addr = s.accept()
        print('Connected to: ', addr[0], addr[1])
        start_new_thread(clientMain,(client,))
    s.close()

if __name__ == '__main__':
    Main()
