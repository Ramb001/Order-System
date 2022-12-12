order = list()
orders = list()

def stack(tableNum, name, category, position, amount):
    if len(order) != 0:
        if tableNum == order[0]:
            flag = False
            for i in range(2, len(order)):
                if category in order[i] and position in order[i]:
                    index = i
                    temp = int(order[index][2]) + int(amount)
                    order[index][2] = str(temp)
                    break
            else:
                flag = True
            if flag:
                pos = [category, position, amount]
                order.append(pos)
        else:
            order.clear()
            order.append(tableNum)
            order.append(name)
            pos = [category, position, amount]
            order.append(pos)
    else:
        order.append(tableNum)
        order.append(name)
        pos = [category, position, amount]
        order.append(pos)
        
def add():
    orders.append(tuple(order))