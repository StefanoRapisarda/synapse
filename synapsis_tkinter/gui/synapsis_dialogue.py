# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'synapsis_dialogue.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1386, 724)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeViewEntriesLeft = QtWidgets.QTreeView(self.centralwidget)
        self.treeViewEntriesLeft.setGeometry(QtCore.QRect(230, 60, 421, 241))
        self.treeViewEntriesLeft.setObjectName("treeViewEntriesLeft")
        self.treeViewEntriesRight = QtWidgets.QTreeView(self.centralwidget)
        self.treeViewEntriesRight.setGeometry(QtCore.QRect(740, 60, 421, 241))
        self.treeViewEntriesRight.setObjectName("treeViewEntriesRight")
        self.plainTextEditTextLeft = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditTextLeft.setGeometry(QtCore.QRect(230, 340, 441, 121))
        self.plainTextEditTextLeft.setObjectName("plainTextEditTextLeft")
        self.plainTextEditTextRight = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditTextRight.setGeometry(QtCore.QRect(720, 340, 431, 121))
        self.plainTextEditTextRight.setObjectName("plainTextEditTextRight")
        self.listWidgetAttributeLeft = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetAttributeLeft.setGeometry(QtCore.QRect(230, 500, 441, 171))
        self.listWidgetAttributeLeft.setObjectName("listWidgetAttributeLeft")
        self.listWidgetAttributeRight = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetAttributeRight.setGeometry(QtCore.QRect(720, 500, 431, 171))
        self.listWidgetAttributeRight.setObjectName("listWidgetAttributeRight")
        self.lineEditSearchFieldLeft = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSearchFieldLeft.setGeometry(QtCore.QRect(230, 10, 113, 20))
        self.lineEditSearchFieldLeft.setObjectName("lineEditSearchFieldLeft")
        self.pushButtonSearchFieldLeft = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearchFieldLeft.setGeometry(QtCore.QRect(340, 10, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearchFieldLeft.setFont(font)
        self.pushButtonSearchFieldLeft.setDefault(False)
        self.pushButtonSearchFieldLeft.setFlat(False)
        self.pushButtonSearchFieldLeft.setObjectName("pushButtonSearchFieldLeft")
        self.pushButtonSearchTextLeft = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearchTextLeft.setGeometry(QtCore.QRect(560, 10, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearchTextLeft.setFont(font)
        self.pushButtonSearchTextLeft.setDefault(False)
        self.pushButtonSearchTextLeft.setFlat(False)
        self.pushButtonSearchTextLeft.setObjectName("pushButtonSearchTextLeft")
        self.lineEditSearchTextLeft = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSearchTextLeft.setGeometry(QtCore.QRect(450, 10, 113, 20))
        self.lineEditSearchTextLeft.setObjectName("lineEditSearchTextLeft")
        self.pushButtonSearchFieldRight = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearchFieldRight.setGeometry(QtCore.QRect(850, 10, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearchFieldRight.setFont(font)
        self.pushButtonSearchFieldRight.setDefault(False)
        self.pushButtonSearchFieldRight.setFlat(False)
        self.pushButtonSearchFieldRight.setObjectName("pushButtonSearchFieldRight")
        self.lineEditSearchFieldRight = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSearchFieldRight.setGeometry(QtCore.QRect(740, 10, 113, 20))
        self.lineEditSearchFieldRight.setObjectName("lineEditSearchFieldRight")
        self.lineEditSearchTextRight = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSearchTextRight.setGeometry(QtCore.QRect(960, 10, 113, 20))
        self.lineEditSearchTextRight.setObjectName("lineEditSearchTextRight")
        self.pushButtonSearchTextRight = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearchTextRight.setGeometry(QtCore.QRect(1070, 10, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearchTextRight.setFont(font)
        self.pushButtonSearchTextRight.setDefault(False)
        self.pushButtonSearchTextRight.setFlat(False)
        self.pushButtonSearchTextRight.setObjectName("pushButtonSearchTextRight")
        self.labelEntriesLeft = QtWidgets.QLabel(self.centralwidget)
        self.labelEntriesLeft.setGeometry(QtCore.QRect(240, 40, 41, 21))
        self.labelEntriesLeft.setAutoFillBackground(True)
        self.labelEntriesLeft.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelEntriesLeft.setObjectName("labelEntriesLeft")
        self.labelEntriesRight = QtWidgets.QLabel(self.centralwidget)
        self.labelEntriesRight.setGeometry(QtCore.QRect(740, 40, 41, 21))
        self.labelEntriesRight.setAutoFillBackground(True)
        self.labelEntriesRight.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelEntriesRight.setObjectName("labelEntriesRight")
        self.labelTextLeft = QtWidgets.QLabel(self.centralwidget)
        self.labelTextLeft.setGeometry(QtCore.QRect(240, 320, 31, 21))
        self.labelTextLeft.setAutoFillBackground(True)
        self.labelTextLeft.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelTextLeft.setObjectName("labelTextLeft")
        self.labelTextRight = QtWidgets.QLabel(self.centralwidget)
        self.labelTextRight.setGeometry(QtCore.QRect(730, 320, 31, 21))
        self.labelTextRight.setAutoFillBackground(True)
        self.labelTextRight.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelTextRight.setObjectName("labelTextRight")
        self.labelAttributesLeft = QtWidgets.QLabel(self.centralwidget)
        self.labelAttributesLeft.setGeometry(QtCore.QRect(240, 480, 101, 21))
        self.labelAttributesLeft.setAutoFillBackground(True)
        self.labelAttributesLeft.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelAttributesLeft.setObjectName("labelAttributesLeft")
        self.labelAttributesRight = QtWidgets.QLabel(self.centralwidget)
        self.labelAttributesRight.setGeometry(QtCore.QRect(730, 480, 101, 21))
        self.labelAttributesRight.setAutoFillBackground(True)
        self.labelAttributesRight.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelAttributesRight.setObjectName("labelAttributesRight")
        self.pushButtonMakeLink = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMakeLink.setGeometry(QtCore.QRect(650, 120, 91, 32))
        self.pushButtonMakeLink.setObjectName("pushButtonMakeLink")
        self.pushButtonRemoveLink = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRemoveLink.setGeometry(QtCore.QRect(650, 150, 91, 32))
        self.pushButtonRemoveLink.setObjectName("pushButtonRemoveLink")
        self.pushButtonShowLink = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonShowLink.setGeometry(QtCore.QRect(650, 180, 91, 32))
        self.pushButtonShowLink.setObjectName("pushButtonShowLink")
        self.pushButtonEditLink = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEditLink.setGeometry(QtCore.QRect(650, 210, 91, 32))
        self.pushButtonEditLink.setObjectName("pushButtonEditLink")
        self.labelLinks = QtWidgets.QLabel(self.centralwidget)
        self.labelLinks.setGeometry(QtCore.QRect(680, 100, 41, 16))
        self.labelLinks.setObjectName("labelLinks")
        self.groupBoxFieldsLeft = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxFieldsLeft.setGeometry(QtCore.QRect(10, 10, 211, 621))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxFieldsLeft.setFont(font)
        self.groupBoxFieldsLeft.setObjectName("groupBoxFieldsLeft")
        self.comboBoxFieldsLeft = QtWidgets.QComboBox(self.groupBoxFieldsLeft)
        self.comboBoxFieldsLeft.setGeometry(QtCore.QRect(10, 30, 151, 31))
        self.comboBoxFieldsLeft.setObjectName("comboBoxFieldsLeft")
        self.pushButtonAddFieldLeft = QtWidgets.QPushButton(self.groupBoxFieldsLeft)
        self.pushButtonAddFieldLeft.setEnabled(True)
        self.pushButtonAddFieldLeft.setGeometry(QtCore.QRect(160, 30, 51, 32))
        self.pushButtonAddFieldLeft.setObjectName("pushButtonAddFieldLeft")
        self.line_1 = QtWidgets.QFrame(self.groupBoxFieldsLeft)
        self.line_1.setGeometry(QtCore.QRect(0, 60, 211, 16))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.scrollAreaLeft = QtWidgets.QScrollArea(self.groupBoxFieldsLeft)
        self.scrollAreaLeft.setGeometry(QtCore.QRect(0, 70, 211, 531))
        self.scrollAreaLeft.setWidgetResizable(True)
        self.scrollAreaLeft.setObjectName("scrollAreaLeft")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 209, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.lineEditField1Left = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditField1Left.setGeometry(QtCore.QRect(10, 30, 151, 21))
        self.lineEditField1Left.setObjectName("lineEditField1Left")
        self.labelField1Left = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelField1Left.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.labelField1Left.setObjectName("labelField1Left")
        self.pushButtonDelField1Left = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonDelField1Left.setEnabled(True)
        self.pushButtonDelField1Left.setGeometry(QtCore.QRect(160, 30, 41, 21))
        self.pushButtonDelField1Left.setObjectName("pushButtonDelField1Left")
        self.lineEndField1Left = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.lineEndField1Left.setGeometry(QtCore.QRect(-3, 60, 211, 20))
        self.lineEndField1Left.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineEndField1Left.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineEndField1Left.setObjectName("lineEndField1Left")
        self.pushButtonDelField2Left = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonDelField2Left.setEnabled(True)
        self.pushButtonDelField2Left.setGeometry(QtCore.QRect(160, 100, 41, 21))
        self.pushButtonDelField2Left.setObjectName("pushButtonDelField2Left")
        self.lineEndField2Left = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.lineEndField2Left.setGeometry(QtCore.QRect(-3, 130, 211, 20))
        self.lineEndField2Left.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineEndField2Left.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineEndField2Left.setObjectName("lineEndField2Left")
        self.lineEditField2Left = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditField2Left.setGeometry(QtCore.QRect(10, 100, 151, 21))
        self.lineEditField2Left.setObjectName("lineEditField2Left")
        self.labelField2Left = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelField2Left.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.labelField2Left.setObjectName("labelField2Left")
        self.scrollAreaLeft.setWidget(self.scrollAreaWidgetContents)
        self.pushButtonEditEntryLeft = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEditEntryLeft.setGeometry(QtCore.QRect(10, 630, 211, 31))
        self.pushButtonEditEntryLeft.setObjectName("pushButtonEditEntryLeft")
        self.pushButtonAddEntryLeft = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddEntryLeft.setGeometry(QtCore.QRect(10, 650, 211, 31))
        self.pushButtonAddEntryLeft.setObjectName("pushButtonAddEntryLeft")
        self.pushButtonAddEntryRight = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddEntryRight.setGeometry(QtCore.QRect(1170, 650, 211, 31))
        self.pushButtonAddEntryRight.setObjectName("pushButtonAddEntryRight")
        self.groupBoxFieldsRight = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxFieldsRight.setGeometry(QtCore.QRect(1170, 10, 211, 621))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxFieldsRight.setFont(font)
        self.groupBoxFieldsRight.setObjectName("groupBoxFieldsRight")
        self.comboBoxFieldsRight = QtWidgets.QComboBox(self.groupBoxFieldsRight)
        self.comboBoxFieldsRight.setGeometry(QtCore.QRect(10, 30, 151, 31))
        self.comboBoxFieldsRight.setObjectName("comboBoxFieldsRight")
        self.pushButtonAddFieldRight = QtWidgets.QPushButton(self.groupBoxFieldsRight)
        self.pushButtonAddFieldRight.setEnabled(True)
        self.pushButtonAddFieldRight.setGeometry(QtCore.QRect(160, 30, 51, 32))
        self.pushButtonAddFieldRight.setObjectName("pushButtonAddFieldRight")
        self.line_2 = QtWidgets.QFrame(self.groupBoxFieldsRight)
        self.line_2.setGeometry(QtCore.QRect(0, 60, 211, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.scrollAreaRight = QtWidgets.QScrollArea(self.groupBoxFieldsRight)
        self.scrollAreaRight.setGeometry(QtCore.QRect(0, 70, 211, 531))
        self.scrollAreaRight.setWidgetResizable(True)
        self.scrollAreaRight.setObjectName("scrollAreaRight")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 209, 529))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.lineEditField1Right = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEditField1Right.setGeometry(QtCore.QRect(10, 30, 151, 21))
        self.lineEditField1Right.setObjectName("lineEditField1Right")
        self.labelField1Right = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.labelField1Right.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.labelField1Right.setObjectName("labelField1Right")
        self.pushButtonDelField1Right = QtWidgets.QPushButton(self.scrollAreaWidgetContents_5)
        self.pushButtonDelField1Right.setEnabled(True)
        self.pushButtonDelField1Right.setGeometry(QtCore.QRect(160, 30, 41, 21))
        self.pushButtonDelField1Right.setObjectName("pushButtonDelField1Right")
        self.lineEndField1Right = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.lineEndField1Right.setGeometry(QtCore.QRect(-3, 60, 211, 20))
        self.lineEndField1Right.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineEndField1Right.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineEndField1Right.setObjectName("lineEndField1Right")
        self.scrollAreaRight.setWidget(self.scrollAreaWidgetContents_5)
        self.pushButtonEditEntryRight = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEditEntryRight.setGeometry(QtCore.QRect(1170, 630, 211, 31))
        self.pushButtonEditEntryRight.setObjectName("pushButtonEditEntryRight")
        self.pushButtonResetEntryLeft = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonResetEntryLeft.setGeometry(QtCore.QRect(10, 610, 211, 31))
        self.pushButtonResetEntryLeft.setObjectName("pushButtonResetEntryLeft")
        self.pushButtonResetEntryRight = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonResetEntryRight.setGeometry(QtCore.QRect(1170, 610, 211, 31))
        self.pushButtonResetEntryRight.setObjectName("pushButtonResetEntryRight")
        self.labelAttributesRight.raise_()
        self.labelAttributesLeft.raise_()
        self.labelTextRight.raise_()
        self.labelTextLeft.raise_()
        self.labelEntriesRight.raise_()
        self.labelEntriesLeft.raise_()
        self.treeViewEntriesLeft.raise_()
        self.treeViewEntriesRight.raise_()
        self.plainTextEditTextLeft.raise_()
        self.plainTextEditTextRight.raise_()
        self.listWidgetAttributeLeft.raise_()
        self.listWidgetAttributeRight.raise_()
        self.lineEditSearchFieldLeft.raise_()
        self.pushButtonSearchFieldLeft.raise_()
        self.pushButtonSearchTextLeft.raise_()
        self.lineEditSearchTextLeft.raise_()
        self.pushButtonSearchFieldRight.raise_()
        self.lineEditSearchFieldRight.raise_()
        self.lineEditSearchTextRight.raise_()
        self.pushButtonSearchTextRight.raise_()
        self.pushButtonMakeLink.raise_()
        self.pushButtonRemoveLink.raise_()
        self.pushButtonShowLink.raise_()
        self.pushButtonEditLink.raise_()
        self.labelLinks.raise_()
        self.groupBoxFieldsLeft.raise_()
        self.pushButtonEditEntryLeft.raise_()
        self.pushButtonAddEntryLeft.raise_()
        self.pushButtonAddEntryRight.raise_()
        self.groupBoxFieldsRight.raise_()
        self.pushButtonEditEntryRight.raise_()
        self.pushButtonResetEntryLeft.raise_()
        self.pushButtonResetEntryRight.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1386, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.menuFile.addAction(self.actionsave)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonSearchFieldLeft.setText(_translate("MainWindow", "Search Field"))
        self.pushButtonSearchTextLeft.setText(_translate("MainWindow", "Search Text"))
        self.pushButtonSearchFieldRight.setText(_translate("MainWindow", "Search Field"))
        self.pushButtonSearchTextRight.setText(_translate("MainWindow", "Search Text"))
        self.labelEntriesLeft.setText(_translate("MainWindow", "Entries"))
        self.labelEntriesRight.setText(_translate("MainWindow", "Entries"))
        self.labelTextLeft.setText(_translate("MainWindow", "Text"))
        self.labelTextRight.setText(_translate("MainWindow", "Text"))
        self.labelAttributesLeft.setText(_translate("MainWindow", "Other attributes"))
        self.labelAttributesRight.setText(_translate("MainWindow", "Other attributes"))
        self.pushButtonMakeLink.setText(_translate("MainWindow", "make"))
        self.pushButtonRemoveLink.setText(_translate("MainWindow", "remove"))
        self.pushButtonShowLink.setText(_translate("MainWindow", "show"))
        self.pushButtonEditLink.setText(_translate("MainWindow", "edit"))
        self.labelLinks.setText(_translate("MainWindow", "Links"))
        self.groupBoxFieldsLeft.setTitle(_translate("MainWindow", "Fields"))
        self.pushButtonAddFieldLeft.setText(_translate("MainWindow", "+"))
        self.labelField1Left.setText(_translate("MainWindow", "TextLabel"))
        self.pushButtonDelField1Left.setText(_translate("MainWindow", "-"))
        self.pushButtonDelField2Left.setText(_translate("MainWindow", "-"))
        self.labelField2Left.setText(_translate("MainWindow", "TextLabel"))
        self.pushButtonEditEntryLeft.setText(_translate("MainWindow", "Edit Entry"))
        self.pushButtonAddEntryLeft.setText(_translate("MainWindow", "Add Entry"))
        self.pushButtonAddEntryRight.setText(_translate("MainWindow", "Add Entry"))
        self.groupBoxFieldsRight.setTitle(_translate("MainWindow", "Fields"))
        self.pushButtonAddFieldRight.setText(_translate("MainWindow", "+"))
        self.labelField1Right.setText(_translate("MainWindow", "TextLabel"))
        self.pushButtonDelField1Right.setText(_translate("MainWindow", "-"))
        self.pushButtonEditEntryRight.setText(_translate("MainWindow", "Edit Entry"))
        self.pushButtonResetEntryLeft.setText(_translate("MainWindow", "Reset"))
        self.pushButtonResetEntryRight.setText(_translate("MainWindow", "Edit Entry"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionsave.setText(_translate("MainWindow", "save"))
