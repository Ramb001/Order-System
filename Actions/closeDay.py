from Actions.stackOrder import orders
from DB.dbVisitors import cur3, con3
from DB.dbMenu import cur2


def calculate():
    if len(orders) != 0:
        money = 0
        prof = 0
        for i in range(len(orders)):
            for row in cur2.execute('SELECT price FROM menu WHERE name = ?;', (orders[i][2][1],)):
                money += (row[0] * int(orders[i][2][2]))
                prof += (row[0] * int(orders[i][2][2]))
                
            for row in cur3.execute('SELECT money FROM visitors WHERE name = ?;', (orders[i][1],)):
                money += row[0]
            cur3.execute('UPDATE visitors SET money = ? WHERE name = ?;', (money, orders[i][1]))
            con3.commit()
            money = 0
        orders.clear()
        
        return prof