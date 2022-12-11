from DB import dbVisitors


def add(surname, name):
    newUser = (surname, name, '0')
    dbVisitors.cur3.execute("INSERT OR REPLACE INTO visitors VALUES(?, ?, ?);", newUser)
    dbVisitors.con3.commit()