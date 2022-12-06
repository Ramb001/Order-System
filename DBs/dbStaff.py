import sqlite3


con = sqlite3.connect('staff.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS staff(
    post TEXT,
    login_id INT PRIMARY KEY UNIQUE,
    password INT);
    """)
con.commit()


staff = [('director', '777', '555'), ('administator', '111', '222'), ('waiter', '001', '001')]
cur.executemany("INSERT INTO staff VALUES(?, ?, ?);", staff)
