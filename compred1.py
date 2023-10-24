import sys
import os
from compred import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton_5.clicked.connect(self.ming)
     self.ui.pushButton.clicked.connect(self.oing)
     self.ui.pushButton_2.clicked.connect(self.dtp)
     self.ui.pushButton_3.clicked.connect(self.repo)
      

  def ming(self):
    os.system("python maining1.py")

  def oing(self):
    os.system("python othring1.py")

  def dtp(self):
    os.system("python dtc1.py")

  def repo(self):
    os.system("python report1.py")


    
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
