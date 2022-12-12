from DB.dbVisitors import cur3


def getVisitors():
    visitors = list(str())
    for row in cur3.execute('SELECT name FROM visitors;'):
            visitors.append(row[0])
            
    res = list(str())
    for i in visitors:
        if i not in res:
            res.append(i)
    
    return res