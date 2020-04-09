import socket

from _thread import *
import threading

print_lock = threading.Lock()

def storeSubmission(c):
    data = c.recv(8)
    filename = str(data.decode('ascii'))
    data = c.recv(8)
    filesize = int(data.decode('ascii'))
    file = open(filename, 'wb')
    l = c.recv(1024)
    total = 1024
    while(total <= filesize):
        print("Receiving....")
        file.write(l)
        l = c.recv(1024)
        total = total + 1024
    file.write(l)
    file.close()
    print("Done Receiving")
    
    
def clientMain(c):
    while True:
        try:
            data = c.recv(1024)
            message = str(data.decode('ascii'))
            if not message:
                print('Bye')
            print('Received from the client:', message)
            if message.lower().strip() == "submission":
                storeSubmission(c)
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
        client, addr = s.accept()
        print('Connected to: ', addr[0], addr[1])
        start_new_thread(clientMain,(client,))
    s.close()

if __name__ == '__main__':
    Main()
