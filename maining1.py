import sys
import os
from maining import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('concrete1')


class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues)
     self.ui.pushButton_2.clicked.connect(self.deletevalues)

  def insertvalues(self):
    with con:
      cur = con.cursor()
      s1 = str(self.ui.lineEdit_4.text())
      s2 = str(self.ui.lineEdit_5.text())
      s3 = str(self.ui.lineEdit_6.text())
      s4 = str(self.ui.lineEdit_8.text())
      cur.execute('INSERT INTO mainingr VALUES(?,?,?,?)',(s1,s2,s3,s4))
      print('Values Successfully Inserted in Database table')
      con.commit()
	  
  def deletevalues(self):
    with con:
      cur = con.cursor()
      cur.execute('DELETE FROM mainingr ')
      print('Values Successfully Deleted From Database table')
      con.commit()


if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
