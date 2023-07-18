# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dbjson.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget, QCheckBox)

import json, uuid, time

from controls.controller import app_screen_geometry, dbRead, returnObj

class Ui_MainFrame(object):
    def setupUi(self, MainFrame):
        if not MainFrame.objectName():
            MainFrame.setObjectName(u"MainFrame")

        app_geometry = app_screen_geometry(QApplication.instance())
        width = int(app_geometry.width() / 1.8)
        height = int(app_geometry.height() / 3)
        # print(width, height)
        MainFrame.resize(width, height)
        MainFrame.setStyleSheet(u"QFrame#Frame{\n"
"	background-color: rgb(255, 250, 194);\n"
"}")
        self.horizontalLayout = QHBoxLayout(MainFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Form = QFrame(MainFrame)
        self.Form.setObjectName(u"Form")
        self.Form.setFrameShape(QFrame.StyledPanel)
        self.Form.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.label)

        self.frame_3 = QFrame(self.Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.username = QLineEdit(self.frame_10)
        self.username.setObjectName(u"username")

        self.horizontalLayout_5.addWidget(self.username)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.name = QLineEdit(self.frame_11)
        self.name.setObjectName(u"name")

        self.horizontalLayout_6.addWidget(self.name)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.mobile = QLineEdit(self.frame_5)
        self.mobile.setObjectName(u"mobile")

        self.horizontalLayout_2.addWidget(self.mobile)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.zipCode = QLineEdit(self.frame_6)
        self.zipCode.setObjectName(u"zipCode")

        self.horizontalLayout_3.addWidget(self.zipCode)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 55))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Clear = QPushButton(self.frame_9)
        self.Clear.setObjectName(u"Clear")

        self.horizontalLayout_4.addWidget(self.Clear)

        self.Proceed = QPushButton(self.frame_9)
        self.Proceed.setObjectName(u"Proceed")

        self.horizontalLayout_4.addWidget(self.Proceed)


        self.verticalLayout_3.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.Form)

        self.frame_2 = QFrame(MainFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 388, 234))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

    # card
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout_5.addLayout(self.formLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame_2)
        #loading the form
        # retreive data
        userList = self.userList()
        # print(userList) -> ['marvin', 'ram']
        self.loadOnce(userList=userList)


        self.retranslateUi(MainFrame)

        QMetaObject.connectSlotsByName(MainFrame)
    # setupUi

    # button connection
        self.Clear.clicked.connect(self.clearForm)
        self.Proceed.clicked.connect(self.editOrWriteData)

    def retranslateUi(self, MainFrame):
        MainFrame.setWindowTitle(QCoreApplication.translate("MainFrame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("MainFrame", u"DATA UPLOAD FORM", None))
        self.label_7.setText(QCoreApplication.translate("MainFrame", u"Username :", None))
        self.label_8.setText(QCoreApplication.translate("MainFrame", u"Name :", None))
        self.label_3.setText(QCoreApplication.translate("MainFrame", u"Mobile no :", None))
        self.label_4.setText(QCoreApplication.translate("MainFrame", u"Zip Code :", None))
        self.Clear.setText(QCoreApplication.translate("MainFrame", u"Clear the Form", None))
        self.Proceed.setText(QCoreApplication.translate("MainFrame", u"Submit the Form", None))
        self.label_2.setText(QCoreApplication.translate("MainFrame", u"DATA RETRIEVE SHOWCASE LIST", None))
    # retranslateUi

    # controllers
    
    def clearForm(self):
        self.username.clear()
        self.name.clear()
        self.mobile.clear()
        self.zipCode.clear()
        self.username.setEnabled(True)
    def loadOnce(self, userList):

        # showData = QtWidgets.QFormLayout()
        # showData.setObjectName("showData")
        # self.verticalLayout_5.addLayout(showData)
        # print(userList)/
        # # Creating card List
        if userList:
            for i in range(len(userList[0])):
                # Card Component
                # print(i) -> 0, 1 ...
                cardLayout = QHBoxLayout()
                cardLayout.setObjectName(f"{i}")
                checkUser = QCheckBox(f"{userList[0][i]}")
                checkUser.setObjectName(f"show_{userList[0][i]}")
                editbtn = QPushButton("Edit")
                editbtn.setObjectName(f"edit_{userList[0][i]}")
                delbtn = QPushButton("Delete")
                delbtn.setObjectName(f"del_{userList[0][i]}")

                editbtn.released.connect(self.edit)
                delbtn.clicked.connect(self.delete)

                cardLayout.addWidget(checkUser)
                cardLayout.addWidget(editbtn)
                cardLayout.addWidget(delbtn)
                # EndCard
                self.formLayout.addRow(cardLayout)
    def userList(self):
        users = []
        userId = []
        dbdata = None
        try:
            dbdata = dbRead(file="db.json")
        except Exception as e:
            print(e)
        if dbdata:
            for count in range(len(dbdata)):
                users.append(dbdata[count]["Username"])
                userId.append(dbdata[count]["userId"])
            return [users, userId]
        else:
            with open("db.json", "w") as dbFile:
                json.dump([], dbFile, indent=4)
                dbFile.close()
            return None
    
    def addUser(self, userData):
        userObj = None
        originalUserObj = None
        # Check Existing USer
        userObject = userData["Username"]
        db = dbRead(file="db.json")
        try:
            originalUserObj = returnObj(jsondb=db, usernm=userObject)
        except Exception as e:
            pass
        userObj = originalUserObj
        if userObj is not None:
            cardComponents = self.formItem(unm=userObj["Username"])
            cardComponents[0].setText(userObj["Username"])
            cardComponents[0].setObjectName(f"show_{userObj['Username']}")

            cardComponents[1].setObjectName(f"edit_{userObj['Username']}")

            cardComponents[2].setObjectName(f"delete_{userObj['Username']}")

            # print(originalUserObj)
            with open("db.json", "r") as dbJson:
                dbdata = json.load(dbJson)
                dbdata.remove(originalUserObj)

                userObj["Username"] = userData["Username"]
                userObj["Name"] = userData["Name"]
                userObj["Mobile"] = userData["Mobile"]
                userObj["ZipCode"] = userData["ZipCode"]

                dbdata.append(userObj)

                with open("db.json", "w") as dbFile:
                    json.dump(dbdata, dbFile, indent=4)
                    dbFile.close()
            self.username.setEnabled(True)
            self.clearForm()
        else:
            cardLayout = QHBoxLayout()
            cardLayout.setObjectName(f"{len(userData) + 1}")

            checkUser = QCheckBox(f"{userData['Username']}")
            checkUser.setObjectName(f"show_{userData['Username']}")

            editbtn = QPushButton("Edit")
            editbtn.setObjectName(f"edit_{userData['Username']}")

            delbtn = QPushButton("Delete")
            delbtn.setObjectName(f"del_{userData['Username']}")

            cardLayout.addWidget(checkUser)
            cardLayout.addWidget(editbtn)
            cardLayout.addWidget(delbtn)
            # EndCard

            db.append(userData)
            # jsonData = json.dumps(obj=rawData)
            with open("db.json", "w") as dbJson:
                json.dump(db, dbJson, indent=4)
                dbJson.close()
            self.username.setEnabled(True)
            self.clearForm()

            self.formLayout.addRow(cardLayout)

    def editOrWriteData(self):
        user_id = uuid.uuid4().hex
        username = self.username.text()
        name = self.name.text()
        mobile = self.mobile.text()
        zipcode = self.zipCode.text()
        rawData = {
            "userId": user_id,
            "Username": username,
            "Name": name,
            "Mobile": mobile,
            "ZipCode": zipcode,
        }

        self.addUser(userData=rawData)
    
    def edit(self):
        self.username.setEnabled(False)
        editBtnSignal = QApplication.focusWidget().objectName().split("_")
        # print(editBtnSignal)

        if "edit" == editBtnSignal[0]:
            existingUser = editBtnSignal[1]
            db = dbRead(file="db.json")
            userObj = returnObj(jsondb=db, usernm=existingUser)
            # print(userObj)

            self.username.setText(f"{userObj['Username']}")
            self.name.setText(f"{userObj['Name']}")
            self.mobile.setText(f"{userObj['Mobile']}")
            self.zipCode.setText(f"{userObj['ZipCode']}")

            username = self.username.text()
            name = self.name.text()
            mobile = self.mobile.text()
            zipcode = self.zipCode.text()

            # print(username, name)

            # save data
            userObj["Username"] = username
            userObj["Name"] = name
            userObj["Mobile"] = mobile
            userObj["ZipCode"] = zipcode

            # print(userObj)

            # rawData = {
            #     "Username": username,
            #     "Name": name,
            #     "Mobile": mobile,
            #     "ZipCode": zipcode,
            # }

            # self.addUser(userData=rawData)
            # db.append(rawData)
            # # jsonData = json.dumps(obj=rawData)
            # with open("db.json", "w+") as dbJson:
            #     json.dump(db, dbJson, indent=4)
            #     dbJson.close()

    def delete(self):
        # print(QtWidgets.QApplication.focusWidget().objectName())
        delBtnSignal = QApplication.focusWidget().objectName().split("_")
        # print(delBtnSignal)
        if "del" == delBtnSignal[0]:
            existingUser = delBtnSignal[1]
            db = dbRead(file="db.json")
            userObj = returnObj(jsondb=db, usernm=existingUser)
            tempObj = userObj
            if userObj in db:
                db.remove(userObj)

                with open("db.json", "w") as dbFile:
                    json.dump(db, dbFile, indent=4)
                    dbFile.close()

                cardId = None  # -> check, edit, delete
                listitem = self.formLayout.children()
                # print(unm)
                for i in range(len(listitem)):
                    # print(listitem[i].objectName())
                    # print(listitem[i].itemAt(0).widget().text())
                    # print(unm == listitem[i].itemAt(0).widget().text())
                    if userObj["Username"] == listitem[i].itemAt(0).widget().text():
                        cardId = listitem[i]
                    #     cardItem.append(listitem[i].itemAt(0).widget())
                    #     cardItem.append(listitem[i].itemAt(1).widget())
                    #     cardItem.append(listitem[i].itemAt(2).widget())
                # print(cardId)
                self.formLayout.removeRow(cardId)
            else:
                # print("pass")
                pass

        # time.sleep(0.1)
        # print(self.formLayout.children())
        # print(self.formLayout.children().itemAt(1))
        # print(self.formLayout.itemAt(1).itemAt(0).widget())
        # print(self.formLayout.itemAt(1).itemAt(1).widget())
        # print(self.formLayout.itemAt(1).itemAt(2).widget())
        # # print(self.formLayout.itemAt(1).itemAt(3))  ->   None
        # print(self)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainFrame = QFrame()
    ui = Ui_MainFrame()
    ui.setupUi(MainFrame)
    MainFrame.show()
    sys.exit(app.exec())