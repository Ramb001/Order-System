import json
import sqlite3


con2 = sqlite3.connect('menu.db')
cur2 = con2.cursor()


def createMenu():
    cur2.execute("""CREATE TABLE IF NOT EXISTS menu(
            category TEXT,
            name TEXT PRIMARY KEY UNIQUE,
            weight TEXT,
            price INT);
            """)

    traffic = json.load(open('menu.json'))
    columns = ['name', 'weight', 'price']

    for i in traffic:
        for k, v in traffic[i].items():
            cort = list()
            for j in v:
                names = [d['name'] for d in v]
                weights = [d['weight'] for d in v]
                prices = [d['price'] for d in v]
                for r in range(len(names)):
                    cort.append(k)
                    cort.append(names[r])
                    cort.append(weights[r])
                    cort.append(prices[r])
                    cur2.execute("INSERT OR REPLACE INTO menu VALUES(?, ?, ?, ?);", tuple(cort))
                    con2.commit()
                    cort = list()