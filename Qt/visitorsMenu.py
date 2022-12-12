from calendar import c
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QTableWidget, QApplication, QPushButton, QTableWidgetItem

from DB import dbVisitors
from Qt.createVisitor import CreateVisitor


class VisitorsMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.centralwidget = QWidget()
        self.gridLayout = QGridLayout()
        self.setWindowTitle("Visitors")
        
        self.columns = ['Visitor', 'Spent money']
        self.table = QTableWidget()
        self.table.setColumnCount(len(self.columns))
        self.table.setHorizontalHeaderLabels(self.columns)
        self.table.resizeColumnsToContents()
        self.createTable()
        
        self.createButton = QPushButton()
        self.createButton.setText("Create")
        self.createButton.clicked.connect(self.create)
        
        self.gridLayout.addWidget(self.table, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.createButton, 1, 0, 1, 1)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)
        
    def createTable(self):
        dbVisitors.cur3.execute('''SELECT * FROM visitors''')
        self.table.setRowCount(0)
        for row, form in enumerate(dbVisitors.cur3):
            self.table.insertRow(row)
            for column, item in enumerate(form):
                self.table.setItem(row, column, QTableWidgetItem(str(item)))
    
    def create(self):
        self.createVisitor = CreateVisitor()
        self.createVisitor.show()
        self.createTable