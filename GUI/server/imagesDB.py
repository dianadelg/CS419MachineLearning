#login dependencies
import sqlite3
import time
import os

#Creating DB file, and creating table
conn = sqlite3.connect('SUBMISSIONS.db')
c = conn.cursor()

#Create table and passes if already created to avoid error
try:
    c.execute('''CREATE TABLE images(username, image_name)''')
except sqlite3.OperationalError:
    pass

def registerImage(uN,iN):
    try:
        c.execute("INSERT INTO images(username, image_name) VALUES(?, ?)", (uN, iN))
        conn.commit()   
    except sqlite3.Error as e:
        print("Register DB Error:", e)
