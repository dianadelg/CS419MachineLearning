#login dependencies
import sqlite3
import time
import os

#Creating DB file, and creating table
conn = sqlite3.connect('USERS.db')
c = conn.cursor()

#Create table and passes if already created to avoid error
try:
    c.execute('''CREATE TABLE users(username, password)''')
except sqlite3.OperationalError:
    pass

#Registers user into DB
def register_DB(un, pw): 
    try:
        c.execute("INSERT INTO users(username, password) VALUES(?, ?)", (un, pw))
        conn.commit()
        print("Account Registered Successfully!")
        login(un,pw) 
    except sqlite3.Error as e:
        print("Register DB Error:", e)
        return False
#Logging in from the registered info
def login(un, pw):
    try:
        c.execute("SELECT username, password FROM users WHERE username = '" + un +  "'AND password='" + pw +"'")
    except sqlite3.Error as e:
        print("Login Error:", e)
        return False
    DBuser = c.fetchone()
    if(DBuser != None):
        print("Login Successful!!")
        return True
    else:
        print("Try Again!! You might have typed in the wrong username or password!!")
        return False

#Logging in from the client typed info
def login():
    un = input("Please Type In Your Username:\n")
    pw = input("Please Type In Your Password:\n")
    try:
        c.execute("SELECT username, password FROM users WHERE username = '" + un +  "'AND password='" + pw +"'")
    except sqlite3.Error as e:
        print("Login Error:", e)
        return False
    DBuser = c.fetchone()
    if(DBuser != None):
        print("Login Successful!!")
        return True
    else:
        print("Try Again!! You might have typed in the wrong username or password!!")
        return False
#Gets credentials from user input
def register_user():
    username = input("Please Create Username:\n")
    password = input("Please Create Password:\n")
    confirmed = input("Please Confirm Password:\n")

    if(not(password == confirmed)):
        print("Passwords Do Not match!")
        time.sleep(2)
        register_user() #restart process

    else:
        un = username
        pw = password
        register_DB(username,password) #TODO: REMOVE DUPLICATES ---> maybe use a set() ?
    
    #login(username,password)

#Main Function
def main():
    register_user()
    
if __name__ == "__main__":
    main()
