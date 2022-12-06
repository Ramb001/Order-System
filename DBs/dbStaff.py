import sqlite3

con = sqlite3.connect('staff.db')
cur = con.cursor()

def createStaff():
    cur.execute("""CREATE TABLE IF NOT EXISTS staff(
        post TEXT,
        id TEXT PRIMARY KEY UNIQUE,
        password TEXT);
        """)
    con.commit()

    staff = [('director', '777', '555'), ('adminstrator', '111', '222'), ('waiter', '001', '001')]
    cur.executemany("INSERT OR REPLACE INTO staff VALUES(?, ?, ?);", staff)
    con.commit()