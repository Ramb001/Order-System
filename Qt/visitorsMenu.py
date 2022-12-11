from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QTableWidget, QApplication, QPushButton


class VisitorsMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.centralwidget = QWidget()
        self.gridLayout = QGridLayout()
        
        self.columns = ['Surname', 'Name', 'Spent money']
        self.table = QTableWidget()
        self.table.setColumnCount(len(self.columns))
        self.table.setHorizontalHeaderLabels(self.columns)
        self.table.resizeColumnsToContents()
        
        self.createButton = QPushButton()
        self.createButton.setText("Create")
        
        self.gridLayout.addWidget(self.table, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.createButton, 1, 0, 1, 1)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)
        
if __name__ == "__main__":
    app = QApplication([""])
    w = VisitorsMenu()
    w.show()
    app.exec_()