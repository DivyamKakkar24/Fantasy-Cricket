# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fantasy_cricket.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(899, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.t5 = QtWidgets.QLineEdit(self.centralwidget)
        self.t5.setObjectName("t5")
        self.horizontalLayout_9.addWidget(self.t5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.t6 = QtWidgets.QLineEdit(self.centralwidget)
        self.t6.setObjectName("t6")
        self.horizontalLayout_9.addWidget(self.t6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.rb1 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rb1.setFont(font)
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_10.addWidget(self.rb1)
        self.rb2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rb2.setFont(font)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_10.addWidget(self.rb2)
        self.rb3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rb3.setFont(font)
        self.rb3.setObjectName("rb3")
        self.horizontalLayout_10.addWidget(self.rb3)
        self.rb4 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rb4.setFont(font)
        self.rb4.setObjectName("rb4")
        self.horizontalLayout_10.addWidget(self.rb4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.setObjectName("list1")
        self.verticalLayout_3.addWidget(self.list1)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.t7 = QtWidgets.QLineEdit(self.centralwidget)
        self.t7.setObjectName("t7")
        self.horizontalLayout_11.addWidget(self.t7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setObjectName("list2")
        self.verticalLayout_5.addWidget(self.list2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t2.setObjectName("t2")
        self.horizontalLayout.addWidget(self.t2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.t3 = QtWidgets.QLineEdit(self.centralwidget)
        self.t3.setObjectName("t3")
        self.horizontalLayout.addWidget(self.t3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.t4 = QtWidgets.QLineEdit(self.centralwidget)
        self.t4.setObjectName("t4")
        self.horizontalLayout.addWidget(self.t4)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem10, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.popups)

        self.rb1.toggled.connect(self.available_players)
        self.rb2.toggled.connect(self.available_players)
        self.rb3.toggled.connect(self.available_players)
        self.rb4.toggled.connect(self.available_players)

        self.list1.itemDoubleClicked.connect(self.removelist1)
        self.list2.itemDoubleClicked.connect(self.removelist2)

        self.points_used=0
        self.available_points=1000
        self.bat=0
        self.bwl=0
        self.wk=0
        self.ar=0
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def message(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle('ATTENTION!')
        Dialog.exec()


    def popups(self,action):
        txt=(action.text())
        if txt=='NEW Team':
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.points_used=0
            self.available_points=1000
            name,OK=QtWidgets.QInputDialog.getText(MainWindow, "Team Name", "Enter name of Team:")
            if OK==True:
                nm=name
                self.t7.setText(nm)
                self.total()
                self.list1.clear()
                self.list2.clear()
                
        if txt=='SAVE Team':
            count = self.list2.count()
            members=''
            for i in range(count):
                members += self.list2.item(i).text()
                if i < count:
                    members += ','
            self.save_team(self.t7.text(),members,self.points_used)

        if txt=='EVALUATE Team':
            from evaluate import Ui_evaluate
            Dialog=QtWidgets.QDialog()
            ui=Ui_evaluate()
            ui.setupUi(Dialog)
            Dialog.exec()

        if txt=='OPEN Team':
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.points_used=0
            self.available_points=1000
            self.list1.clear()
            self.list2.clear()
            self.total()
            self.open_team()


    def open_team(self):
        MyFantasy=sqlite3.connect("Fantasy_Cricket.db")
        curf=MyFantasy.cursor()
        sql = "SELECT Name from Teams;"
        curf.execute(sql)
        record=curf.fetchall()
        teams=[]
        for rec in record:
            teams.append(rec[0])
        Team,OK=QtWidgets.QInputDialog.getItem(MainWindow, "Dream Team", "Choose your Team:",teams,0,False)
        if OK==True and Team:
            self.t7.setText(Team)
        else:
            return

        curf.execute("SELECT * from Teams WHERE Name='"+Team+"';")
        rec=curf.fetchone()
        players=rec[1].split(',')
        self.list2.addItems(players)
        self.points_used=rec[2]
        self.available_points=1000-rec[2]

        count=self.list2.count()
        for i in range(count-1):
            name=self.list2.item(i).text()
            sql="SELECT * from Stats WHERE Player='"+name+"';"
            curf.execute(sql)
            record=curf.fetchone()
            major=record[6]
            if major=='BAT':
                self.bat+=1
            elif major=='BWL':
                self.bwl+=1
            elif major=='AR':
                self.ar+=1
            elif major=='WK':
                self.wk+=1
        self.total()
        MyFantasy.close()

            
    def save_team(self,name,players,total):
        if self.bat+self.bwl+self.ar+self.wk<11:
            msg='Insufficient Players'
            self.message(msg)
            return
        MyFantasy=sqlite3.connect("Fantasy_Cricket.db")
        curf=MyFantasy.cursor()
        sql = "INSERT INTO Teams (Name,Players,Value) VALUES ('"+name+"','"+players+"','"+str(total)+"');"
        try:
            curf.execute(sql)
            MyFantasy.commit()
            self.message("Team saved successfully")
            MyFantasy.close()
        except:
            print("Error in Operation")
            self.message("Error in Operation")
            MyFantasy.rollback()
        
    def total(self):
        self.t1.setText(str(self.bat))
        self.t2.setText(str(self.bwl))
        self.t3.setText(str(self.ar))
        self.t4.setText(str(self.wk))
        self.t5.setText(str(self.available_points))
        self.t6.setText(str(self.points_used))


    def logic(self,ctg,item):
        msg=''
        if ctg=='BAT' and self.bat>=5:
            msg='Maximum 5 batsmmen allowed'
        elif ctg=='BWL' and self.bwl>=5:
            msg='Maximum 5 bowlers allowed'
        elif ctg=='AR' and self.ar>=3:
            msg='Maximum 3 Allrounders allowed'
        elif ctg=='WK' and self.wk>=1:
            msg='Maximum 1 Wicketkeeper allowed'
            
        if msg != '':
            self.message(msg)
            return False
        
        if self.available_points <=  0:
            msg='No more points left!'
            self.message(msg)
            return False

        count=self.list2.count()
        for i in range(count):
            if item.text() in self.list2.item(i).text():
                msg='Player already selected'
                self.message(msg)
                return False

        MyFantasy=sqlite3.connect("Fantasy_Cricket.db")
        curf=MyFantasy.cursor()
        curf.execute("SELECT * from Stats where Player='"+item.text()+"'")
        record=curf.fetchone()
        if self.available_points-int(record[5]) > 0:
            self.available_points -= int(record[5])
            self.points_used += int(record[5])
            if ctg=='BAT':
                self.bat+=1
            elif ctg=='BWL':
                self.bwl+=1
            elif ctg=='WK':
                self.wk+=1
            elif ctg=='AR':
                self.ar+=1   
            MyFantasy.close()
            return True
        else:
            msg='Insufficient Points'
            self.message(msg)
            return False       

    def available_players(self):
        if self.rb1.isChecked()==True:
            self.list1.clear()
            MyFantasy=sqlite3.connect("Fantasy_Cricket.db")
            curf=MyFantasy.cursor()
            curf.execute("SELECT * from Stats")
            record=curf.fetchall()
            for rec in record:
                if rec[6]=='BAT':
                    self.list1.addItem(rec[0])
            MyFantasy.close()
        elif self.rb2.isChecked()==True:
            self.list1.clear()
            MyFantasy=sqlite3.connect("Fantasy_Cricket.db")
            curf=MyFantasy.cursor()
            curf.execute("SELECT * from Stats")
            record=curf.fetchall()
            for rec in record:
                if rec[6]=='BWL':
                    self.list1.addItem(rec[0])
            MyFantasy.close()
        elif self.rb3.isChecked()==True:
            self.list1.clear()
            MyFantasy=sqlite3.connect("Fantasy_Cricket.db")
            curf=MyFantasy.cursor()
            curf.execute("SELECT * from Stats")
            record=curf.fetchall()
            for rec in record:
                if rec[6]=='AR':
                    self.list1.addItem(rec[0])
            MyFantasy.close()
        elif self.rb4.isChecked()==True:
            self.list1.clear()
            MyFantasy=sqlite3.connect("Fantasy_Cricket.db")
            curf=MyFantasy.cursor()
            curf.execute("SELECT * from Stats")
            record=curf.fetchall()
            for rec in record:
                if rec[6]=='WK':
                    self.list1.addItem(rec[0])
            MyFantasy.close()


    def removelist1(self,item):
        ctg=''
        if self.rb1.isChecked()==True:
            ctg='BAT'
        if self.rb2.isChecked()==True:
            ctg='BWL'
        if self.rb3.isChecked()==True:
            ctg='AR'
        if self.rb4.isChecked()==True:
            ctg='WK'  
        check=self.logic(ctg,item)
        if check == True:
            self.list1.takeItem(self.list1.row(item))
            self.list2.addItem(item.text())
            self.total()
    
    def removelist2(self,item):
        self.list2.takeItem(self.list2.row(item))
        k=item.text()
        MyFantasy=sqlite3.connect("Fantasy_Cricket.db")
        curf=MyFantasy.cursor()
        curf.execute("SELECT * from Stats where Player='"+k+"'")
        record=curf.fetchone()
        self.points_used -= record[5]
        self.available_points += record[5]
        if record[6]=='BAT':
            self.bat-=1
        if record[6]=='BWL':
            self.bwl-=1
        if record[6]=='AR':
            self.ar-=1
        if record[6]=='WK':
            self.wk-=1
        MyFantasy.close()
        self.total()
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Points Available"))
        self.label_11.setText(_translate("MainWindow", "Points Used"))
        self.rb1.setText(_translate("MainWindow", "BAT"))
        self.rb2.setText(_translate("MainWindow", "BOW"))
        self.rb3.setText(_translate("MainWindow", "AR"))
        self.rb4.setText(_translate("MainWindow", "WK"))
        self.label_10.setText(_translate("MainWindow", ">"))
        self.label_12.setText(_translate("MainWindow", "Team Name"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.label_2.setText(_translate("MainWindow", "Batsman (BAT)"))
        self.label_3.setText(_translate("MainWindow", "Bowlers (BOWL)"))
        self.label_4.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.label_5.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionNEW_Team.setShortcut(_translate("MainWindow", "Alt+N"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
