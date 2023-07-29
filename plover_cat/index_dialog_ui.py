# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plover_cat\index_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_indexDialog(object):
    def setupUi(self, indexDialog):
        indexDialog.setObjectName("indexDialog")
        indexDialog.resize(448, 305)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(indexDialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(indexDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.indexChoice = QtWidgets.QComboBox(indexDialog)
        self.indexChoice.setObjectName("indexChoice")
        self.horizontalLayout_3.addWidget(self.indexChoice)
        self.addNewIndex = QtWidgets.QPushButton(indexDialog)
        self.addNewIndex.setObjectName("addNewIndex")
        self.horizontalLayout_3.addWidget(self.addNewIndex)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_2 = QtWidgets.QLabel(indexDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.indexPrefix = QtWidgets.QLineEdit(indexDialog)
        self.indexPrefix.setObjectName("indexPrefix")
        self.horizontalLayout_4.addWidget(self.indexPrefix)
        self.hideDescript = QtWidgets.QCheckBox(indexDialog)
        self.hideDescript.setEnabled(True)
        self.hideDescript.setChecked(True)
        self.hideDescript.setTristate(False)
        self.hideDescript.setObjectName("hideDescript")
        self.horizontalLayout_4.addWidget(self.hideDescript)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.formLayout)
        self.label_3 = QtWidgets.QLabel(indexDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.displayEntries = QtWidgets.QTableWidget(indexDialog)
        self.displayEntries.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.displayEntries.setObjectName("displayEntries")
        self.displayEntries.setColumnCount(0)
        self.displayEntries.setRowCount(0)
        self.verticalLayout.addWidget(self.displayEntries)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(indexDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.entryText = QtWidgets.QLineEdit(indexDialog)
        self.entryText.setObjectName("entryText")
        self.horizontalLayout.addWidget(self.entryText)
        self.entryAdd = QtWidgets.QPushButton(indexDialog)
        self.entryAdd.setEnabled(False)
        self.entryAdd.setObjectName("entryAdd")
        self.horizontalLayout.addWidget(self.entryAdd)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.saveAndInsert = QtWidgets.QPushButton(indexDialog)
        self.saveAndInsert.setEnabled(False)
        self.saveAndInsert.setObjectName("saveAndInsert")
        self.verticalLayout_2.addWidget(self.saveAndInsert)
        self.saveIndex = QtWidgets.QPushButton(indexDialog)
        self.saveIndex.setObjectName("saveIndex")
        self.verticalLayout_2.addWidget(self.saveIndex)
        self.buttonBox = QtWidgets.QDialogButtonBox(indexDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(indexDialog)
        self.buttonBox.rejected.connect(indexDialog.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(indexDialog)

    def retranslateUi(self, indexDialog):
        _translate = QtCore.QCoreApplication.translate
        indexDialog.setWindowTitle(_translate("indexDialog", "Dialog"))
        self.label.setText(_translate("indexDialog", "Index:"))
        self.addNewIndex.setText(_translate("indexDialog", "Add New Index"))
        self.label_2.setText(_translate("indexDialog", "Prefix:"))
        self.hideDescript.setText(_translate("indexDialog", "Hide entry descriptions"))
        self.label_3.setText(_translate("indexDialog", "Entries for index:"))
        self.displayEntries.setToolTip(_translate("indexDialog", "Double-click to edit index entry descriptions."))
        self.displayEntries.setSortingEnabled(True)
        self.label_4.setText(_translate("indexDialog", "Index entry text:"))
        self.entryAdd.setText(_translate("indexDialog", "Add new entry"))
        self.saveAndInsert.setText(_translate("indexDialog", "Save && Insert"))
        self.saveIndex.setText(_translate("indexDialog", "Save"))
