from DB import dbVisitors


def createPerson(surname, name):
    person = (surname, name, '0')
    res = dbVisitors.cur.execute("SELECT * FROM visitors WHERE post = ? and id = ? and password = ?", (person[0], person[1], person[2],))
    if res.fetchone() is not None:
        return True