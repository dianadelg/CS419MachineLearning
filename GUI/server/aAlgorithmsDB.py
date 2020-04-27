import sqlite3
import time
import os

#Creating DB file, and creating table
conn = sqlite3.connect('SUBMISSIONS.db')
c = conn.cursor()

#Create table and passes if already created to avoid error
try:
    c.execute('''CREATE TABLE attacks(username, attack_name)''')
except sqlite3.OperationalError:
    pass

def registerAttack(uN,aN):
    try:
        c.execute("INSERT INTO attacks(username, attack_name) VALUES(?, ?)", (uN, aN))
        conn.commit()   
    except sqlite3.Error as e:
        print("Register DB Error:", e)
        
def getAttacks():
    try:
        c.execute('''SELECT attack_name FROM attacks''')
        return c.fetchall()
    except sqlite3.Error as e:
        print(e)
