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
    except sqlite3.Error as e:
        print("Register DB Error:", e)

#Loggin in, gets info from DB file
def login(un,pw):
    try:
        c.execute("SELECT username, password FROM users WHERE username =" + un +  "AND password=" + pw)
        print("Login Succesful! Welcome!")
    except sqlite3.Error as e:
        print("Login Error:", e)

#Gets credentials from user input
def register_user():
    username = input("Please Create Username: ")
    password = input("Please Create Password: ")
    confirmed = input("Please Confirm Password: ")

    if(not(password == confirmed)):
        print("Passwords Do Not match!")
        time.sleep(2)
        register_user() #restart process

    else:
        register_DB(username,password) #TODO: REMOVE DUPLICATES ---> maybe use a set() ?
    
    #login(username,password)

#Main Function
def main():
    register_user()
    
if __name__ == "__main__":
    main()
