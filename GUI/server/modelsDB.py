#login dependencies
import sqlite3
import time
import os

#Creating DB file, and creating table
conn = sqlite3.connect('SUBMISSIONS.db')
c = conn.cursor()

#Create table and passes if already created to avoid error
try:
    c.execute('''CREATE TABLE models(username, model_name, model_accuracy)''')
except sqlite3.OperationalError:
    pass

def registerModel(uN,mN,mA):
    try:
        c.execute("INSERT INTO models(username, model_name, model_accuracy) VALUES(?, ?, ?)", (uN, mN, mA))
        conn.commit()   
    except sqlite3.Error as e:
        print("Register DB Error:", e)
        
def getModels():
    try:
        c.execute('''SELECT model_name FROM models''')
        return c.fetchall()
    except sqlite3.Error as e:
        print(e)
 '''    
def getModels():
    try:
        return c.fetchall()
    except sqlite3.Error as e:
        print(e)
        
def getModels():
    try:
        return c.fetchall()
    except sqlite3.Error as e:
        print(e)
'''