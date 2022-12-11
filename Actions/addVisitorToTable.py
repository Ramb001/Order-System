from DB.dbVisitors import cur3
from PyQt5.QtWidgets import QTableWidgetItem

def add(x):
    cur3.execute('''SELECT * FROM visitors''')
    x.setRowCount(0)
    for row, form in enumerate(cur3):
        x.insertRow(row)
        for column, item in enumerate(form):
            print(str(item))
            x.setItem(row, column, QTableWidgetItem(str(item))) 