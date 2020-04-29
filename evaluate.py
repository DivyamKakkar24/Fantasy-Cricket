# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_evaluate(object):
    def setupUi(self, evaluate):
        evaluate.setObjectName("evaluate")
        evaluate.resize(700, 364)
        self.gridLayout = QtWidgets.QGridLayout(evaluate)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(evaluate)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.combo1 = QtWidgets.QComboBox(evaluate)
        self.combo1.setObjectName("combo1")
        self.combo1.addItem("")
        MyFantasy=sqlite3.connect("Fantasy_Cricket.db")
        self.horizontalLayout_3.addWidget(self.combo1)
        curf=MyFantasy.cursor()
        curf.execute("SELECT * from Teams")
        record=curf.fetchall()
        for rec in record:
            self.combo1.addItem(rec[0])
        MyFantasy.close()
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.combo2 = QtWidgets.QComboBox(evaluate)
        self.combo2.setObjectName("combo2")
        self.combo2.addItem("")
        self.combo2.addItem("")
        self.horizontalLayout_2.addWidget(self.combo2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line = QtWidgets.QFrame(evaluate)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(evaluate)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.list3 = QtWidgets.QListWidget(evaluate)
        self.list3.setObjectName("list3")
        self.verticalLayout_2.addWidget(self.list3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(evaluate)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.t9 = QtWidgets.QLineEdit(evaluate)
        self.t9.setObjectName("t9")
        self.horizontalLayout_6.addWidget(self.t9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.list4 = QtWidgets.QListWidget(evaluate)
        self.list4.setObjectName("list4")
        self.verticalLayout_3.addWidget(self.list4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.b1 = QtWidgets.QPushButton(evaluate)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.horizontalLayout_7.addWidget(self.b1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.b1.clicked.connect(self.analysis)

        self.retranslateUi(evaluate)
        QtCore.QMetaObject.connectSlotsByName(evaluate)


    def points(self):
        self.list4.clear()
        self.sum = 0
        count=self.list3.count()
        for i in range(count):
            name=self.list3.item(i).text()
            if name=='MS Dhoni':
                self.list4.addItem('92')
                self.sum+=92
            elif name=='Virat Kohli':
                self.list4.addItem('92')
                self.sum+=92
            elif name=='Yuvraj Singh':
                self.list4.addItem('21')
                self.sum+=21
            elif name=='Ajinkya Rahane':
                self.list4.addItem('37')
                self.sum+=37
            elif name=='Shikhar Dhawan':
                self.list4.addItem('22')
                self.sum+=22
            elif name=='Axar Patel':
                self.list4.addItem('24')
                self.sum+=24
            elif name=='Ravindra Jadeja':
                self.list4.addItem('56')
                self.sum+=56
            elif name=='Kedar Jadhav':
                self.list4.addItem('48')
                self.sum+=48
            elif name=='R. Ashwin':
                self.list4.addItem('93')
                self.sum+=93
            elif name=='Umesh Yadav':
                self.list4.addItem('55')
                self.sum+=55
            elif name=='Jaspreet Bumrah':
                self.list4.addItem('10')
                self.sum+=10
            elif name=='Bhuwaneshwar Kumar':
                self.list4.addItem('33')
                self.sum+=33
            elif name=='Rohit Sharma':
                self.list4.addItem('40')
                self.sum+=40
            elif name=='Dinesh Kartik':
                self.list4.addItem('47')
                self.sum+=47
            elif name=='Hardik Pandya':
                self.list4.addItem('44')
                self.sum+=44
            elif name=='Chris Gayle':
                self.list4.addItem('46')
                self.sum+=46
            elif name=='AB de Villiers':
                self.list4.addItem('67')
                self.sum+=67
            elif name=='M. Shami':
                self.list4.addItem('44')
                self.sum+=44
            elif name=='Rishab Pant':
                self.list4.addItem('43')
                self.sum+=43
            elif name=='David Warner':
                self.list4.addItem('33')
                self.sum+=33
            elif name=='Glen Maxwell':
                self.list4.addItem('43')
                self.sum+=43
        self.t9.setText(str(self.sum))


    def analysis(self):
        self.list3.clear()
        team = self.combo1.currentText()
        MyFantasy=sqlite3.connect("Fantasy_Cricket.db")
        curf=MyFantasy.cursor()
        curf.execute("SELECT Players from Teams WHERE Name='"+team+"'")
        record=curf.fetchone()
        selected=record[0].split(',')
        MyFantasy.close()
        self.list3.addItems(selected)
        self.points()
    

    def retranslateUi(self, evaluate):
        _translate = QtCore.QCoreApplication.translate
        evaluate.setWindowTitle(_translate("evaluate", "Form"))
        self.label.setText(_translate("evaluate", "Evaluate the Performance of your Fantasy Team"))
        self.combo1.setItemText(0, _translate("evaluate", "Select Team"))
        self.combo2.setItemText(0, _translate("evaluate", "Select Match"))
        self.combo2.setItemText(1, _translate("evaluate", "Match 1"))
        self.label_2.setText(_translate("evaluate", "Players"))
        self.label_3.setText(_translate("evaluate", "Points"))
        self.b1.setText(_translate("evaluate", "Calculate Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaluate = QtWidgets.QWidget()
    ui = Ui_evaluate()
    ui.setupUi(evaluate)
    evaluate.show()
    sys.exit(app.exec_())
