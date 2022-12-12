from DB.dbVisitors import cur3


def checkVisitor(name):
    res = cur3.execute('SELECT name FROM visitors WHERE name = ?;', (name,))
    if res.fetchone() is not None:
        return True