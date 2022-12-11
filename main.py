from DB.dbStaff import createStaff
from DB.dbMenu import createMenu
from DB.dbVisitors import createVisitors
from Qt.start import run

if __name__ == '__main__':
    createStaff()
    createMenu()
    createVisitors()
    run()