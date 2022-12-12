from DB.dbMenu import cur2

def getNames(category):
    names = list(str())
    for row in cur2.execute('SELECT name FROM menu WHERE category = ?;', (category,)):
            names.append(row[0])
            
    res = list(str())
    for i in names:
        if i not in res:
            res.append(i)
    
    return res