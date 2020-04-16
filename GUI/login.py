#login dependencies
import sqlite3
import time
import os

#Creating DB file, and creating table
conn = sqlite3.connect('USERS.db')
c = conn.cursor()

#Create table and passes if already created to avoid error
try:
    c.execute('''CREATE TABLE Admins(username, password)''')
    c.execute('''CREATE TABLE users(username, password)''')
except sqlite3.OperationalError:
    pass


#Registers user into DB
def register_DB(un, pw): 
    try:
        c.execute("INSERT INTO users(username, password) VALUES(?, ?)", (un, pw))
        conn.commit()
        login(un,pw)
        return "user"    
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
        return "user"
    else:
        try:
            c.execute("SELECT username, password FROM Admins WHERE username = '" + un +  "'AND password='" + pw +"'")
        except sqlite3.Error as e:
            print("Login Error:", e)
            return False
        DBuser = c.fetchone()
        if(DBuser != None):
            return "admin"
        else:
            return False
