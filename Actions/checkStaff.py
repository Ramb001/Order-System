from DB import dbStaff


def checkPerson(post, login, password):
    person = (post, login, password)
    res = dbStaff.cur.execute("SELECT * FROM staff WHERE post = ? and id = ? and password = ?", (person[0], person[1], person[2],))
    if res.fetchone() is not None:
        return True