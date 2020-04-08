import socket
import login as user

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

def Main():
    checkCridentials()
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    message = "I signed in bro"
    while True:
        # message sent to server 
        s.send(message.encode('ascii')) 
  
        # messaga received from server 
        data = s.recv(1024) 
  
        # print the received message 
        # here it would be a reverse of sent message 
        print('Received from the server :',str(data.decode('ascii'))) 
  
        # ask the client whether he wants to continue 
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break  
    s.close()

if __name__ == '__main__':
    Main()
