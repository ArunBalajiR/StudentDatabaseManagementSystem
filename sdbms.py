# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sdbms.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 590)
        MainWindow.setMinimumSize(QtCore.QSize(690, 590))
        MainWindow.setMaximumSize(QtCore.QSize(690, 590))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/sdbmss.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    border-radius:15px;\n"
"    background:red;\n"
"    color:white;\n"
"    \n"
"    background-color: #1a73e8;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius:15px;\n"
"    \n"
"    background-color: rgb(114, 159, 207);\n"
"    color:black;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    border-radius:15px;\n"
"    color:white;\n"
"    background-color: rgb(32, 74, 135);\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFocusPolicy(QtCore.Qt.TabFocus)
        self.frame.setStyleSheet("background-color:rgb(238, 238, 236);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 671, 271))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setGeometry(QtCore.QRect(370, 0, 301, 271))
        self.frame_2.setStyleSheet("QFrame\n"
"{\n"
"    background:rgba(136, 138, 133,0.5);\n"
"    border:none\n"
"    \n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(5)
        self.frame_2.setMidLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame_2)
        self.toolButton_2.setGeometry(QtCore.QRect(0, 10, 51, 31))
        self.toolButton_2.setStyleSheet("background:transparent;\n"
"border:none;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/USERCONTROL.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_2.setObjectName("toolButton_2")
        self.pushButton_clr = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_clr.setGeometry(QtCore.QRect(10, 200, 281, 41))
        self.pushButton_clr.setToolTip("")
        self.pushButton_clr.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: #1a73e8;\n"
"    color:white;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"    \n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgba(26, 115, 232,0.2);\n"
"    color:black;\n"
"\n"
"    \n"
"}\n"
"")
        self.pushButton_clr.setObjectName("pushButton_clr")
        self.pushButton_del = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_del.setGeometry(QtCore.QRect(10, 150, 281, 41))
        self.pushButton_del.setToolTip("")
        self.pushButton_del.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: #1a73e8;\n"
"    color:white;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"    \n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgba(26, 115, 232,0.2);\n"
"    color:black;\n"
"\n"
"    \n"
"}\n"
"")
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_update = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_update.setGeometry(QtCore.QRect(10, 100, 281, 41))
        self.pushButton_update.setToolTip("")
        self.pushButton_update.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: #1a73e8;\n"
"    color:white;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"    \n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgba(26, 115, 232,0.2);\n"
"    color:black;\n"
"\n"
"    \n"
"}\n"
"")
        self.pushButton_update.setObjectName("pushButton_update")
        self.pushButton_save = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_save.setGeometry(QtCore.QRect(10, 50, 281, 41))
        self.pushButton_save.setToolTip("")
        self.pushButton_save.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: #1a73e8;\n"
"    color:white;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"    \n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgba(26, 115, 232,0.2);\n"
"    color:black;\n"
"\n"
"    \n"
"}\n"
"")
        self.pushButton_save.setObjectName("pushButton_save")
        self.lineEdit_search = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_search.setEnabled(True)
        self.lineEdit_search.setGeometry(QtCore.QRect(50, 10, 201, 31))
        self.lineEdit_search.setMouseTracking(True)
        self.lineEdit_search.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_search.setToolTip("")
        self.lineEdit_search.setStyleSheet("QLineEdit\n"
"{\n"
"    background:rgb(238, 238, 236);\n"
"    border-radius:10px;\n"
"    color:#707172;\n"
"    \n"
"}")
        self.lineEdit_search.setFrame(False)
        self.lineEdit_search.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_search.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_search.setClearButtonEnabled(True)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.pushButton_search = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_search.setGeometry(QtCore.QRect(260, 10, 31, 31))
        self.pushButton_search.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: white;\n"
"    color:white;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"     \n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgba(26, 115, 232,0.2);\n"
"    color:black;\n"
"\n"
"    \n"
"}\n"
"")
        self.pushButton_search.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search.setIcon(icon2)
        self.pushButton_search.setObjectName("pushButton_search")
        self.lineEdit_name = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_name.setEnabled(True)
        self.lineEdit_name.setGeometry(QtCore.QRect(10, 60, 341, 31))
        self.lineEdit_name.setMouseTracking(True)
        self.lineEdit_name.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_name.setToolTip("")
        self.lineEdit_name.setStyleSheet("QLineEdit\n"
"{\n"
"    background:rgba(136, 138, 133,0.2);\n"
"    border-radius:10px;\n"
"    color:#707172;\n"
"    \n"
"}")
        self.lineEdit_name.setFrame(False)
        self.lineEdit_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_name.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_name.setClearButtonEnabled(True)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(70, 20, 241, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#1A73E8;")
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(self.frame_3)
        self.toolButton.setGeometry(QtCore.QRect(20, 10, 51, 41))
        self.toolButton.setStyleSheet("background:transparent;\n"
"border:none;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/Caller.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon3)
        self.toolButton.setIconSize(QtCore.QSize(35, 35))
        self.toolButton.setObjectName("toolButton")
        self.lineEdit_rollno = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_rollno.setEnabled(True)
        self.lineEdit_rollno.setGeometry(QtCore.QRect(10, 100, 341, 31))
        self.lineEdit_rollno.setMouseTracking(True)
        self.lineEdit_rollno.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_rollno.setToolTip("")
        self.lineEdit_rollno.setStyleSheet("QLineEdit\n"
"{\n"
"    background:rgba(136, 138, 133,0.2);\n"
"    border-radius:10px;\n"
"    color:#707172;\n"
"    \n"
"}")
        self.lineEdit_rollno.setFrame(False)
        self.lineEdit_rollno.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_rollno.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_rollno.setClearButtonEnabled(True)
        self.lineEdit_rollno.setObjectName("lineEdit_rollno")
        self.lineEdit_course = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_course.setEnabled(True)
        self.lineEdit_course.setGeometry(QtCore.QRect(10, 140, 341, 31))
        self.lineEdit_course.setMouseTracking(True)
        self.lineEdit_course.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_course.setToolTip("")
        self.lineEdit_course.setStyleSheet("QLineEdit\n"
"{\n"
"    background:rgba(136, 138, 133,0.2);\n"
"    border-radius:10px;\n"
"    color:#707172;\n"
"    \n"
"}")
        self.lineEdit_course.setFrame(False)
        self.lineEdit_course.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_course.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_course.setClearButtonEnabled(True)
        self.lineEdit_course.setObjectName("lineEdit_course")
        self.lineEdit_age = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_age.setEnabled(True)
        self.lineEdit_age.setGeometry(QtCore.QRect(10, 180, 341, 31))
        self.lineEdit_age.setMouseTracking(True)
        self.lineEdit_age.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_age.setToolTip("")
        self.lineEdit_age.setStyleSheet("QLineEdit\n"
"{\n"
"    background:rgba(136, 138, 133,0.2);\n"
"    border-radius:10px;\n"
"    color:#707172;\n"
"    \n"
"}")
        self.lineEdit_age.setFrame(False)
        self.lineEdit_age.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_age.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_age.setClearButtonEnabled(True)
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.lineEdit_dob = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_dob.setEnabled(True)
        self.lineEdit_dob.setGeometry(QtCore.QRect(10, 220, 341, 31))
        self.lineEdit_dob.setMouseTracking(True)
        self.lineEdit_dob.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_dob.setToolTip("")
        self.lineEdit_dob.setStyleSheet("QLineEdit\n"
"{\n"
"    background:rgba(136, 138, 133,0.2);\n"
"    border-radius:10px;\n"
"    color:#707172;\n"
"    \n"
"}")
        self.lineEdit_dob.setFrame(False)
        self.lineEdit_dob.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dob.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_dob.setClearButtonEnabled(True)
        self.lineEdit_dob.setObjectName("lineEdit_dob")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 271, 671, 281))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("Header\n"
"{\n"
"color:rgb(114, 159, 207);\n"
"}\n"
"")
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(133)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_clr.pressed.connect(self.lineEdit_name.clear)
        self.pushButton_clr.pressed.connect(self.lineEdit_search.clear)
        self.pushButton_clr.pressed.connect(self.lineEdit_rollno.clear)
        self.pushButton_clr.pressed.connect(self.lineEdit_course.clear)
        self.pushButton_clr.pressed.connect(self.lineEdit_age.clear)
        self.pushButton_clr.pressed.connect(self.lineEdit_dob.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Management System"))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.pushButton_clr.setText(_translate("MainWindow", "Clear"))
        self.pushButton_del.setText(_translate("MainWindow", "Delete"))
        self.pushButton_update.setText(_translate("MainWindow", "Update"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.lineEdit_search.setPlaceholderText(_translate("MainWindow", "Search Name or Rollno"))
        self.lineEdit_name.setPlaceholderText(_translate("MainWindow", "Enter the Name"))
        self.label.setText(_translate("MainWindow", "Enter the Database here:"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.lineEdit_rollno.setPlaceholderText(_translate("MainWindow", "Enter the RollNo."))
        self.lineEdit_course.setPlaceholderText(_translate("MainWindow", "Enter the Course"))
        self.lineEdit_age.setPlaceholderText(_translate("MainWindow", "Enter the Age"))
        self.lineEdit_dob.setPlaceholderText(_translate("MainWindow", "Enter the DOB"))
        self.tableWidget.setToolTip(_translate("MainWindow", "Datatable"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Roll No"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Course"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Age"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "DOB"))

import source

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

