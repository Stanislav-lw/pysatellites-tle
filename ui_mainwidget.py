# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(1024, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWidget.sizePolicy().hasHeightForWidth())
        MainWidget.setSizePolicy(sizePolicy)
        self.mainLayout = QGridLayout(MainWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.labelSpaceTrack = QLabel(MainWidget)
        self.labelSpaceTrack.setObjectName(u"labelSpaceTrack")

        self.mainLayout.addWidget(self.labelSpaceTrack, 0, 0, 1, 1)

        self.userpassLayout = QHBoxLayout()
        self.userpassLayout.setObjectName(u"userpassLayout")
        self.labelUsername = QLabel(MainWidget)
        self.labelUsername.setObjectName(u"labelUsername")

        self.userpassLayout.addWidget(self.labelUsername)

        self.usernameLineEdit = QLineEdit(MainWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.userpassLayout.addWidget(self.usernameLineEdit)

        self.labelPassword = QLabel(MainWidget)
        self.labelPassword.setObjectName(u"labelPassword")

        self.userpassLayout.addWidget(self.labelPassword)

        self.passwordLineEdit = QLineEdit(MainWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.userpassLayout.addWidget(self.passwordLineEdit)


        self.mainLayout.addLayout(self.userpassLayout, 1, 0, 1, 1)

        self.line = QFrame(MainWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.mainLayout.addWidget(self.line, 2, 0, 1, 1)

        self.noradLayout = QHBoxLayout()
        self.noradLayout.setObjectName(u"noradLayout")
        self.labelNorads = QLabel(MainWidget)
        self.labelNorads.setObjectName(u"labelNorads")

        self.noradLayout.addWidget(self.labelNorads)

        self.idsLineEdit = QLineEdit(MainWidget)
        self.idsLineEdit.setObjectName(u"idsLineEdit")

        self.noradLayout.addWidget(self.idsLineEdit)

        self.updatePushButton = QPushButton(MainWidget)
        self.updatePushButton.setObjectName(u"updatePushButton")

        self.noradLayout.addWidget(self.updatePushButton)


        self.mainLayout.addLayout(self.noradLayout, 3, 0, 1, 1)

        self.noradListWidget = QListWidget(MainWidget)
        self.noradListWidget.setObjectName(u"noradListWidget")
        self.noradListWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.noradListWidget.setSelectionMode(QAbstractItemView.MultiSelection)

        self.mainLayout.addWidget(self.noradListWidget, 4, 0, 1, 1)

        self.savePushButton = QPushButton(MainWidget)
        self.savePushButton.setObjectName(u"savePushButton")

        self.mainLayout.addWidget(self.savePushButton, 5, 0, 1, 1)

        self.mwtLayout = QGridLayout()
        self.mwtLayout.setObjectName(u"mwtLayout")

        self.mainLayout.addLayout(self.mwtLayout, 6, 0, 1, 1)


        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Satellite TLE Downloader", None))
        self.labelSpaceTrack.setText(QCoreApplication.translate("MainWidget", u"SpaceTrack", None))
        self.labelUsername.setText(QCoreApplication.translate("MainWidget", u"Username:", None))
        self.labelPassword.setText(QCoreApplication.translate("MainWidget", u"Password:", None))
        self.labelNorads.setText(QCoreApplication.translate("MainWidget", u" Norad ids:", None))
        self.idsLineEdit.setInputMask("")
        self.idsLineEdit.setText("")
        self.idsLineEdit.setPlaceholderText("")
        self.updatePushButton.setText(QCoreApplication.translate("MainWidget", u"Update satellites", None))
        self.savePushButton.setText(QCoreApplication.translate("MainWidget", u"Save selected satellite TLE", None))
    # retranslateUi

