#Author:SercanCelenk
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def window():
    app=QApplication(sys.argv)
    win=QMainWindow()

    win.setWindowTitle("First Application")
    win.setGeometry(150,150,600,600)

    win.show()
    sys.exit(app.exec())

window()
