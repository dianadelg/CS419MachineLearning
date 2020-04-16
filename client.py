import socket
import login as user
import os

global res

BUFFER_SIZE = 4096 # send 4096 bytes each time step
"""
If the user wants to signup an account then the user gets registered into the DB,
and then it gets logged into the GUI, if they want to signin then they just type
in their cridentials and the person gets tracked as they use the client mainly for image,
and model submissions
"""
def checkCridentials():
        res = False
        while True:
            ans = input('Please type signup or signin:\n')#check what process they want to go through
            if ans.lower().strip() == 'signup':#if the user wants to signup
                res = user.register_user()
            elif ans.lower().strip() == 'signin':#if the user wants to signin to a registered account
                res = user.login()
            else:#if they dont type in the right info
                print("ERROR: You Must Type In Signup or Signin First")
                continue
            if res == False:#if the login/registration was successful
                continue
            else:#if the login/registration wasn't successful
                break
"""
If the user wants to submit a model/image then the user types in which one they want to submit
Once they type it in then we send over the file name and size to the server, then we transfer
over the data inside of the file
"""       
def submitModel(s):
        try:
                filename = input("Please type the name of the model/image you want to submit:\n")#get the model/image filename
                s.send(filename.encode('ascii'))#send the filename
                filesize = os.stat(filename).st_size#get the filesize
                s.send(str(filesize).encode('ascii'))#send the filesize
                response = s.recv(1024)#wait for the server response to be ready
                if str(response.decode('ascii')) == 'ready':
                        with open(filename, "rb") as f:#start sending the contents of the file
                                i = 0
                                while (i == 0):
                                        bytes_read = f.read(BUFFER_SIZE)
                                        if not bytes_read:
                                                i = 1
                                        if i == 0:
                                                s.sendall(bytes_read)
                                        count += 1
                                f.close()
        except:
                print("There was an error with the filename. Please try another one or type it in correctly.")
def Main():
    checkCridentials()#Checks if the client has an account or wants to register an account
    host = '127.0.0.1'#host ip address
    port = 12345#connecting port for the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#build the socket that communication will be over
    server.connect((host,port))#attach the host and port to the socket
    while True:#while loop for client commands
        message = input("Type 'submit' to submit a model/image:\n")
        if message.lower().strip() == "submit":
                message = "submission"
                server.send(message.encode('ascii'))#lets the server know that this is a submission process
                submitModel(server)##then starts that process
                data = server.recv(1024)#then waits for the response message to know if everything was sent or not
                if str(data.decode('ascii')) == 'success':#if it was its a success
                        print("image/model was submitted successfully\!!!n")
                else:#if it wasn't
                        print("There was an error submitting")
        # ask the client whether he wants to continue 
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break  
    server.close()

if __name__ == '__main__':
    Main()
