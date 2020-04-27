import socket
import login as user
import os
global server

BUFFER_SIZE1 = 4096 # send 4096 bytes for the models
BUFFER_SIZE2 = 2048 # send 2048 bytes for the images
host = '127.0.0.1'#host ip address
port = 12345#connecting port for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#build the socket that communication will be over
server.connect((host,port))#attach the host and port to the socket
        
def submitModel(FN, uName,MA):
        global server
        message = "submitModel"
        server.send(message.encode('ascii'))
        response = server.recv(1024)#wait for the server response to be ready
        if str(response.decode('ascii')) == 'ready':
              server.send(uName.encode('ascii'))
        response = server.recv(1024)#wait for the server response to be ready
        if str(response.decode('ascii')) == 'ready':
              server.send(str(MA).encode('ascii'))
        response = server.recv(1024)#wait for the server response to be ready
        if str(response.decode('ascii')) == 'ready':
                try:
                        filename = FN
                        server.send(filename.encode('ascii'))#send the filename
                        filesize = os.stat(filename).st_size#get the filesize
                        server.send(str(filesize).encode('ascii'))#send the filesize
                        response = server.recv(1024)#wait for the server response to be ready
                        if str(response.decode('ascii')) == 'ready':
                                with open(filename, "rb") as f:#start sending the contents of the file
                                        i = 0
                                        while (i == 0):
                                                bytes_read = f.read(BUFFER_SIZE1)
                                                if not bytes_read:
                                                        i = 1
                                                if i == 0:
                                                        server.sendall(bytes_read)
                                        f.close()
                except Exception as e:
                        print("There was an error with the filename. Please try another one or type it in correctly. Or,", e)

def submitImage(IN,uName):
        global server
        print(server)
        message = "submitImage"
        server.send(message.encode('ascii'))
        response = server.recv(1024)#wait for the server response to be ready
        if str(response.decode('ascii')) == 'ready':
              server.send(uName.encode('ascii'))  
        response = server.recv(1024)#wait for the server response to be ready
        if str(response.decode('ascii')) == 'ready':
                try:
                        filename = IN
                        server.send(filename.encode('ascii'))#send the filename
                        filesize = os.stat(filename).st_size#get the filesize
                        server.send(str(filesize).encode('ascii'))#send the filesize
                        response = server.recv(1024)#wait for the server response to be ready
                        if str(response.decode('ascii')) == 'ready':
                                with open(filename, "rb") as f:#start sending the contents of the file
                                        i = 0
                                        while (i == 0):
                                                bytes_read = f.read(BUFFER_SIZE2)
                                                if not bytes_read:
                                                        i = 1
                                                if i == 0:
                                                        server.sendall(bytes_read)
                                        f.close()
                except Exception as e:
                        print("There was an error with the filename. Please try another one or type it in correctly. Or, ", e)

def submitDataset(DS):
        global server
        message = "submitDataset"
        server.send(message.encode('ascii')) 
        response = server.recv(1024)#wait for the server response to be ready
        if str(response.decode('ascii')) == 'ready':
                try:
                        filename = DS
                        server.send(filename.encode('ascii'))#send the filename
                        filesize = os.stat(filename).st_size#get the filesize
                        server.send(str(filesize).encode('ascii'))#send the filesize
                        response = server.recv(1024)#wait for the server response to be ready
                        if str(response.decode('ascii')) == 'ready':
                                with open(filename, "rb") as f:#start sending the contents of the file
                                        i = 0
                                        while (i == 0):
                                                bytes_read = f.read(BUFFER_SIZE1)
                                                if not bytes_read:
                                                        i = 1
                                                if i == 0:
                                                        server.sendall(bytes_read)
                                        f.close()
                        return True
                except Exception as e:
                        print("There was an error with the filename. Please try another one or type it in correctly. Or,",e)
                        return False

def getDataset(FN):
    global server
    try:
        message = "getDataset"
        server.send(message.encode('ascii'))
        response = server.recv(1024)#wait for the server response to be ready
        if str(response.decode('ascii')) == 'ready':
              server.send(FN.encode('ascii'))
        data = server.recv(1024)
        filesize = str(data.decode('ascii'))
        filesize = int(filesize)
        ready = "ready"
        server.send(ready.encode('ascii'))
        with open(FN, "wb") as f:
                total = 0
                while (total <= filesize):
                    bytes_read = server.recv(BUFFER_SIZE1)
                    if total <= filesize:
                        f.write(bytes_read)
                    total += BUFFER_SIZE1
                f.close()
    except Exception as e:
        print(e)
                
def getBoard():
    global server
    try:
        message = "getBoard"
        server.send(message.encode('ascii'))
        body = []
        i = 4
        while True:
            ready = "ready"
            server.send(ready.encode())
            table = server.recv(16)#wait for the server response to be ready
            body.append(str(table.decode()))
            if len(body)/i == 20:
               return body
    except Exception as e:
        print("error getting the board information or", e)
    
def getMode():
    try:
        global server
        message = "getMode"
        server.send(message.encode('ascii'))
        mode = server.recv(1024)
        return str(mode.decode('ascii'))
    except Exception as e:
        print(e)

def updateMode(string):
    try:
        global server
        message = "updateMode"
        server.send(message.encode('ascii'))
        response = server.recv(1024)#wait for the server response to be ready
        if str(response.decode('ascii')) == 'ready':
                server.send(string.encode('ascii'))
    except Exception as e:
            print(e)
