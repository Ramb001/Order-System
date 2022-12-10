from Qt.loginMenu import main
from DB.dbStaff import createStaff
from DB.dbMenu import createMenu


if __name__ == '__main__':
    createStaff()
    createMenu()
    main()