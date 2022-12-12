from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QMessageBox

from Qt.visitorsMenu import VisitorsMenu
from Qt.ordersMenu import OrdersMenu
from Actions.closeDay import calculate


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.centralwidget = QWidget()
        self.gridLayout = QGridLayout()
        self.setWindowTitle("Main menu")
        
        self.orders = QPushButton()
        self.orders.setText("Orders")
        
        self.visitors = QPushButton()
        self.visitors.setText("Visitors")
        self.visitors.clicked.connect(self.visitor)
        
        self.profit = QPushButton()
        self.profit.setText("Daily profit")
        self.profit.clicked.connect(self.showProfit)
        
        self.run = QPushButton()
        self.flag = False
        self.profitDigit = 0
        self.run.setText("Day is closed!")
        self.run.clicked.connect(self.changeState)

        self.gridLayout.addWidget(self.orders, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.visitors, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.profit, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.run, 1, 1, 1, 1)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)
            
    def changeState(self):
        self.flag = not self.flag
        if self.flag:
            self.run.setText("Day is opened!")
            self.orders.clicked.connect(self.order)
            self.run.clicked.connect(self.close)
        else:
            self.run.setText("Day is closed!")

    def visitor(self):
        self.visitor = VisitorsMenu()
        self.visitor.show()
        
    def order(self):
        self.orderMenu = OrdersMenu()
        self.orderMenu.show()
        
    def close(self):
        self.profitDigit = calculate()
        
    def showProfit(self):
        msg = QMessageBox()
        msg.setWindowTitle("Daily profit")
        if self.flag:
            text = '0'
        else:
            text = str(self.profitDigit)
        msg.setText(f'{text} Rubles')
        msg.exec_()