import sqlite3 


con3 = sqlite3.connect('visitors.db')
cur3 = con3.cursor()

def createVisitors():
    cur3.execute('''CREATE TABLE IF NOT EXISTS visitors(
        surname TEXT,
        name TEXT,
        money INT)''')
    con3.commit()