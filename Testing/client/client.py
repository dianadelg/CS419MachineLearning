import socket
import login as user
import os
import tqdm

global res

BUFFER_SIZE = 4096 # send 4096 bytes each time step

def checkCridentials():
        res = False
        while True:
            ans = input('Please type signup or signin:\n')
            if ans.lower().strip() == 'signup':
                res = user.register_user()
            elif ans.lower().strip() == 'signin':
                res = user.login()
            else:
                print("ERROR: You Must Type In Signup or Signin First")
                continue
            if res == False:
                continue
            else:
                break
        
def submitModel(s):
        filename = 'mnist_cnn_model.pth '
        s.send(filename.encode('ascii'))
        filesize = os.stat(filename).st_size
        s.send(str(filesize).encode('ascii'))
        response = s.recv(1024)
        if str(response.decode('ascii')) == 'ready':
                with open(filename, "rb") as f:
                        i = 0
                        while (i == 0):
                                bytes_read = f.read(BUFFER_SIZE)
                                if not bytes_read:
                                        i = 1
                                if i == 0:
                                        s.sendall(bytes_read)
                                count += 1
                        f.close()
        
def Main():
    checkCridentials()
    host = '127.0.0.1'
    port = 12345
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host,port))
    while True:
        # message sent to server
        message = input("Do you want to submit a model or image: type model or image")
        if message.lower().strip() == "model":
                message = "submission"
                server.send(message.encode('ascii'))
                submitModel(server)
        #if message.lower().strip() == "image":
                
        #server.send(message.encode('ascii')) 
        print('im out2')
        # message received from server 
        data = server.recv(1024) 
  
        # print the received message 
        # here it would be a reverse of sent message 
        print('Received from the server :',str(data.decode('ascii'))) 
  
        # ask the client whether he wants to continue 
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break  
    server.close()

if __name__ == '__main__':
    Main()
