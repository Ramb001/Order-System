from DB import dbStaff


def add(post, login, password):
    newUser = (post, login, password)
    dbStaff.cur.execute("INSERT OR REPLACE INTO staff VALUES(?, ?, ?);", newUser)
    dbStaff.con.commit()