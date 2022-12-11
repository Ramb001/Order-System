from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton

from Qt.visitorsMenu import VisitorsMenu


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
        
        self.profit = QPushButton()
        self.profit.setText("Daily profit")
        
        self.run = QPushButton()
        self.flag = False
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
            self.visitors.clicked.connect(self.visitor)
        else:
            self.run.setText("Day is closed!")

    def visitor(self):
        self.visitor = VisitorsMenu()
        self.visitor.show()