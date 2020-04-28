import socket
import os
from _thread import *
import threading

print_lock = threading.Lock()

BUFFER_SIZE = 4096 # send 4096 bytes each time step
mode = "White"
uName = ""
mAccuracy = 0
def clientMain(c):
    global uName
    global mAccuracy
    while True:
        print("waiting for message...")
        data = c.recv(64)
        try:
            message = str(data.decode('ascii'))
            message = message.lower().strip()
            print('Received from the client:',message)
            if message == "submitmodel":
                ready = "ready"
                c.send(ready.encode('ascii'))
                data = c.recv(1024)
                uName = str(data.decode('ascii'))
                ready = "ready"
                c.send(ready.encode('ascii'))
                data = c.recv(1024)
                mAccuracy = int(str(data.decode('ascii')))
                ready = "ready"
                c.send(ready.encode('ascii'))
                data = c.recv(1024)
                filename = str(data.decode('ascii'))
                data = c.recv(1024)
                filesize = str(data.decode('ascii'))
                filesize = int(filesize)
                print(uName,mAccuracy,filename,filesize)
                storeModel(c,filesize,filename)
            elif message == "submitimage":
                ready = "ready"
                c.send(ready.encode('ascii'))
                data = c.recv(1024)
                uName = str(data.decode('ascii'))
                ready = "ready"
                c.send(ready.encode('ascii'))
                data = c.recv(1024)
                filename = str(data.decode('ascii'))
                data = c.recv(1024)
                filesize = str(data.decode('ascii'))
                filesize = int(filesize)
                storeImage(c,filesize,filename)
            elif message == "submitattack":
                ready = "ready"
                c.send(ready.encode('ascii'))
                data = c.recv(1024)
                uName = str(data.decode('ascii'))
                ready = "ready"
                c.send(ready.encode('ascii'))
                data = c.recv(1024)
                filename = str(data.decode('ascii'))
                data = c.recv(1024)
                filesize = str(data.decode('ascii'))
                filesize = int(filesize)
                storeAttack(c,filesize,filename)
            elif message == "getmode":
                sendMode(c)
            elif message == "updatemode":
                updateMode(c)
            elif message == "getdataset":
                ready = "ready"
                c.send(ready.encode('ascii'))
                data = c.recv(1024)
                filename = str(data.decode('ascii'))
                sendDataset(c,filename)
            elif message == "getdatasetready":
                ready = "ready"
                c.send(ready.encode('ascii'))
                data = c.recv(1024)
                filename = str(data.decode('ascii'))
                sendDataset(c,filename)
            elif message == "submitdataset":
                ready = "ready"
                c.send(ready.encode('ascii'))
                data = c.recv(1024)
                filename = str(data.decode('ascii'))
                data = c.recv(1024)
                filesize = str(data.decode('ascii'))
                filesize = int(filesize)
                storeDataset(c,filesize,filename)
            elif message == "getboard":
                sendBoard(c)
            elif message == "getmodels":
                sendModels(c)
            elif message == "getattacks":
                sendAttacks(c)
            elif message == "getimages":
                sendImages(c)
            elif message == "readygetmodels":
                sendModels(c)
            elif message == "readygetattacks":
                sendAttacks(c)
            elif message == "readygetimages":
                sendImages(c)
            elif message == "getmodelsready":
                sendModels(c)
            elif message == "getattacksready":
                sendAttacks(c)
            elif message == "getimagesready":
                sendImages(c)
            elif message == "ready":
                continue
            else:
                print("not a proper message,", message)
                c.close()
                continue
        except Exception as e:
            print('Lost connection to the client because of ', e)

def storeImage(c, fs, fn):
    import imagesDB as IDB
    global uName
    try:
        ready = "ready"
        c.send(ready.encode('ascii'))
        direct = "Images/"
        direct += fn
        with open(direct, "wb") as f:
            total = 0
            while (total <= fs):
                bytes_read = c.recv(BUFFER_SIZE)
                if total <= fs:
                    f.write(bytes_read)
                total += BUFFER_SIZE
            f.close()
        IDB.registerImage(uName,fn)
    except Exception as e:
        print("could not receive all of the image. Or, ", e)
       
def storeModel(c, fs, fn):
    import modelsDB as MDB
    global uName
    global mAccuracy
    try:
        ready = "ready"
        c.send(ready.encode('ascii'))
        direct = "Models/"
        direct += fn
        with open(direct, "wb") as f:
            total = 0
            while (total <= fs):
                bytes_read = c.recv(BUFFER_SIZE)
                if total <= fs:
                    f.write(bytes_read)
                total += BUFFER_SIZE
            f.close()
        MDB.registerModel(uName,fn,mAccuracy)
    except Exception as e:
        print("could not receive all of the model. Or, ",e)

def storeDataset(c, fs, fn):
    try:
        ready = "ready"
        c.send(ready.encode('ascii'))
        direct = "Datasets/"
        direct += fn
        with open(direct, "wb") as f:
            total = 0
            while (total <= fs):
                bytes_read = c.recv(BUFFER_SIZE)
                if total <= fs:
                    f.write(bytes_read)
                total += BUFFER_SIZE
            f.close()
    except Exception as e:
        print("could not receive all of the model. Or, ", e)     
        
def storeAttack(c, fs, fn):
    import aAlgorithmsDB as AADB
    global uName
    try:
        ready = "ready"
        c.send(ready.encode('ascii'))
        direct = "Attacks/"
        direct += fn
        with open(direct, "wb") as f:
            total = 0
            while (total <= fs):
                bytes_read = c.recv(BUFFER_SIZE)
                if total <= fs:
                    f.write(bytes_read)
                total += BUFFER_SIZE
            f.close()
        AADB.registerAttack(uName, fn)
    except Exception as e:
        print("could not receive all of the model. Or, ", e) 

def sendDataset(c, fn):
        direct = "Datasets/"
        direct += fn
        try:
                filename = direct
                filesize = os.stat(filename).st_size#get the filesize
                c.send(str(filesize).encode('ascii'))#send the filesize
                response = c.recv(1024)#wait for the server response to be ready
                if str(response.decode('ascii')) == 'ready':
                        with open(filename, "rb") as f:#start sending the contents of the file
                                i = 0
                                while (i == 0):
                                        bytes_read = f.read(BUFFER_SIZE)
                                        if not bytes_read:
                                                i = 1
                                        if i == 0:
                                                c.sendall(bytes_read)
                                f.close()
        except Exception as e:
                print("There was an error with the filename. Please try another one or type it in correctly. Or, ",e)

def sendBoard(c):
    import leaderboardDB as LDB
    try:
        info = LDB.getLeaderboard()
        i = 0
        j = 0
        while i < len(info) and i < 20:
            j = 0
            while j < len(info[i]):
                response = c.recv(1024)#wait for the server response to be ready
                if str(response.decode()) == 'ready':
                    c.send(info[i][j].encode())
                j += 1
            i += 1
        bye = "bye"
        c.send(bye.encode())
    except Exception as e:
        print(e)
def sendAttacks(c):
    import aAlgorithmsDB as AADB
    try:
        info = AADB.getAttacks()
        i = 0
        while i < len(info):
            c.send(info[i][0].encode())
            i += 1
        bye = "bye"
        c.send(bye.encode())
    except Exception as e:
        print(e)

def sendModels(c):
    import modelsDB as MDB
    try:
        if mode == "White":
            info = MDB.getModelsW()
        elif mode == "Gray":
            info = MDB.getModelsG()
        elif mode == "Black":
            info = MDB.getModelsB()
        i = 0
        while i < len(info):
            c.send(info[i][0].encode())
            i += 1
            response = c.recv(1024)#wait for the server response to be ready
            if str(response.decode()) == 'ready':
                continue
        bye = "bye"
        c.send(bye.encode())
    except Exception as e:
        print(e)
        
def sendImages(c):
    import imagesDB as IDB
    try:
        info = IDB.getImages()
        i = 0
        while i < len(info):
            c.send(info[i][0].encode())
            i += 1
        bye = "bye"
        c.send(bye.encode())
    except Exception as e:
        print(e)

def updateMode(c):
    try:
        ready = "ready"
        c.send(ready.encode('ascii'))
        newMode = c.recv(32)
        global mode
        mode = str(newMode.decode('ascii'))
    except Exception as e:
        print(e)

def sendMode(c):
    try:
        c.send(mode.encode('ascii'))
    except Exception as e:
        print(e)

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
