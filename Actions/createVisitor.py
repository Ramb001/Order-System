from DB import dbVisitors


def add(name):
    newUser = (name, '0')
    dbVisitors.cur3.execute("INSERT OR REPLACE INTO visitors VALUES(?, ?);", newUser)
    dbVisitors.con3.commit()