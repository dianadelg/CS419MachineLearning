import socket
import login as user
import os

global res

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
        filename = 'login.py '
        s.send(filename.encode('ascii'))
        filesize = os.stat(filename).st_size
        s.send(str(filesize).encode('ascii'))
        file = open('login.py', 'rb')
        l = file.read(1024)
        while (l):
                print('Sending...')
                s.send(l)
                l = f.read(1024)
        file.close()
         print ('Done Sending!!')
        
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
