#login dependencies
import sqlite3
import time
import os

#Creating DB file, and creating table
conn = sqlite3.connect('LEADERBOARD.db')
c = conn.cursor()

#Create table and passes if already created to avoid error
try:
    c.execute('''CREATE TABLE Leaderboard(username, model_name, model_accuracy, attack_percent)''')
except sqlite3.OperationalError as e:
    pass

def insertNewAttack(uN, mN, mA, aP):
    try:
        c.execute("INSERT INTO datasets(username, model_name, model_accuracy, attack_percent) VALUES(?, ?, ?, ?)", (uN, mN, mA, aP))
        conn.commit() 
    except sqlite3.Error as e:
        print("Register DB Error:", e)


def getLeaderboard():
    try:
        c.execute('''SELECT * FROM leaderboard ORDER BY  attack_percent DESC;''')
        data = c.fetchall()
        return data 
    except sqlite3.Error as e:
        print(e)