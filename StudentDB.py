from PyQt5.QtGui import *
from PyQt5.QtWidgets import  *
from PyQt5.QtCore import *
import sqlite3
from PyQt5 import QtWidgets
from sdbms import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_update.clicked.connect(self.loadData)
        self.pushButton_save.clicked.connect(self.SaveData)
        self.pushButton_del.clicked.connect(self.DelData)
        self.pushButton_search.clicked.connect(self.Search)
    def center(self,QMessageBox):
        QMessageBox.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                QMessageBox.size(),
                QtWidgets.qApp.desktop().availableGeometry()
            )
        )

    def loadData(self):
        try:

            connect=sqlite3.connect('/home/arunadhigaaram/SQLite/student.db')
            mycursor=connect.cursor()
            exe = "SELECT * FROM student"
            result=mycursor.execute(exe)
            self.tableWidget.setRowCount(0)   #before we load data we declare our table's row count = 0
            for rowno,rowdata in enumerate(result):   #refer demo file for know about enumurate function
                self.tableWidget.insertRow(rowno)
                for colno,data in enumerate(rowdata):
                    self.tableWidget.setItem(rowno,colno,QtWidgets.QTableWidgetItem(str(data)))   #we cannot directly add it ..so we access it using qtwidgets.qtablewidgetitem and then converting our data into sting
            QMessageBox.information(QMessageBox(),'Successfull','The Student Table is Updated')
            mycursor.close()
        except Exception:
            QMessageBox.warning(QMessageBox(),'Error !',' Could not Update')


    def SaveData(self):
        name=self.lineEdit_name.text()
        roll=self.lineEdit_rollno.text()
        course=self.lineEdit_course.text()
        age=self.lineEdit_age.text()
        dob=self.lineEdit_dob.text()
        try:
            connect=sqlite3.connect('/home/arunadhigaaram/SQLite/student.db')
            cur=connect.cursor()
            cur.execute('insert into student values(?,?,?,?,?)',(name,roll,course,age,dob))
            connect.commit()
            QMessageBox.information(QMessageBox(), 'Successful', 'Student is added successfully to the database.')
        except Exception:
            QMessageBox.warning(QMessageBox(),'Error', 'Could not add student to the database.Try Again!')
        cur.close()
    def DelData(self):
        try:
            name = self.lineEdit_name.text()
            roll = self.lineEdit_rollno.text()
            course = self.lineEdit_course.text()
            age = self.lineEdit_age.text()
            dob = self.lineEdit_dob.text()
            connect = sqlite3.connect('/home/arunadhigaaram/SQLite/student.db')
            cur = connect.cursor()
            cur.execute('delete from STUDENT where NAME=?', (name,))
            cur.execute('delete from STUDENT where ROLLNO=?', (roll,))
            connect.commit()
            QMessageBox.information(QMessageBox(),'Successful !','Student Entry Deleted')
            cur.close()
        except Exception:
            QMessageBox.warning(QMessageBox(),'Error','Student Data Not Found in Database\nCheck the Spelling')


    def Search(self):
        search=''
        search=self.lineEdit_search.text()

        try:
            sr=int(search)
            connect=sqlite3.connect('/home/arunadhigaaram/SQLite/student.db')
            cur = connect.cursor()
            result = cur.execute('select * from STUDENT where ROLLNO=?',(sr,))
            self.tableWidget.setRowCount(0)
            for rowno, rowdata in enumerate(result):
                self.tableWidget.insertRow(rowno)
                for colno, data in enumerate(rowdata):
                    self.tableWidget.setItem(rowno, colno, QtWidgets.QTableWidgetItem(str(data)))
            QMessageBox.information(QMessageBox(), 'Successfull', 'Search Found ..')
            connect.commit()
            cur.close()
        except Exception:

        # QMessageBox.information(QMessageBox(), 'Successfull', 'Sd Found')

            connect = sqlite3.connect('/home/arunadhigaaram/SQLite/student.db')
            cur = connect.cursor()
            result = cur.execute('select * from STUDENT where NAME=?', (search,))
            self.tableWidget.setRowCount(0)
            for rowno, rowdata in enumerate(result):
                self.tableWidget.insertRow(rowno)
                for colno, data in enumerate(rowdata):
                    self.tableWidget.setItem(rowno, colno, QtWidgets.QTableWidgetItem(str(data)))
            if self.tableWidget.rowCount() < 1:
                QMessageBox.warning(QMessageBox(), 'Error', 'Data Not Found')
            else:
                QMessageBox.information(QMessageBox(), 'Successfull', 'Search Found ..')
            # print(QTableWidget.rowCount())
            connect.commit()
            cur.close()







if __name__=='__main__':
    app=QApplication([])

    window=MainWindow()

    window.show()
    app.exec()