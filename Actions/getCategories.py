from DB.dbMenu import cur2


def getCategories():
    categories = list(str())
    for row in cur2.execute('SELECT category FROM menu;'):
            categories.append(row[0])
            
    res = list(str())
    for i in categories:
        if i not in res:
            res.append(i)
    
    return res