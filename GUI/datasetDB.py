#login dependencies
import sqlite3
import time
import os

#Creating DB file, and creating table
conn = sqlite3.connect('SUBMISSIONS.db')
c = conn.cursor()

#Create table and passes if already created to avoid error
try:
    c.execute('''CREATE TABLE datasets(username, datasetName)''')
except sqlite3.OperationalError:
    pass

def registerDataset(uN, dN):
     try:
        c.execute("INSERT INTO datasets(username, datasetName) VALUES(?, ?)", (uN, dN))
        conn.commit()   
     except sqlite3.Error as e:
        print("Register DB Error:", e)


def getDatasets():
    try:
        c.execute('''SELECT datasetName FROM datasets''')
        return c.fetchall()
    except sqlite3.Error as e:
        print(e)
