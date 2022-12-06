import sqlite3


con = sqlite3.connect('staff.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS staff(
    post TEXT,
    login_id INT,
    password INT);
    """)
con.commit()