# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plover_cat\field_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fieldDialog(object):
    def setupUi(self, fieldDialog):
        fieldDialog.setObjectName("fieldDialog")
        fieldDialog.setWindowModality(QtCore.Qt.WindowModal)
        fieldDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(fieldDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(fieldDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.fieldName = QtWidgets.QLineEdit(fieldDialog)
        self.fieldName.setObjectName("fieldName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fieldName)
        self.label_2 = QtWidgets.QLabel(fieldDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.fieldValue = QtWidgets.QLineEdit(fieldDialog)
        self.fieldValue.setObjectName("fieldValue")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fieldValue)
        self.addNewField = QtWidgets.QPushButton(fieldDialog)
        self.addNewField.setObjectName("addNewField")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.addNewField)
        self.verticalLayout.addLayout(self.formLayout)
        self.userDictTable = QtWidgets.QTableWidget(fieldDialog)
        self.userDictTable.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.userDictTable.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.userDictTable.setTabKeyNavigation(False)
        self.userDictTable.setProperty("showDropIndicator", False)
        self.userDictTable.setDragDropOverwriteMode(False)
        self.userDictTable.setAlternatingRowColors(True)
        self.userDictTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.userDictTable.setObjectName("userDictTable")
        self.userDictTable.setColumnCount(0)
        self.userDictTable.setRowCount(0)
        self.verticalLayout.addWidget(self.userDictTable)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.removeField = QtWidgets.QPushButton(fieldDialog)
        self.removeField.setObjectName("removeField")
        self.horizontalLayout.addWidget(self.removeField)
        self.buttonBox = QtWidgets.QDialogButtonBox(fieldDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(fieldDialog)
        self.buttonBox.accepted.connect(fieldDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(fieldDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(fieldDialog)

    def retranslateUi(self, fieldDialog):
        _translate = QtCore.QCoreApplication.translate
        fieldDialog.setWindowTitle(_translate("fieldDialog", "Field Editor"))
        self.label.setText(_translate("fieldDialog", "Field name:"))
        self.label_2.setText(_translate("fieldDialog", "Field value:"))
        self.addNewField.setText(_translate("fieldDialog", "Add new field"))
        self.userDictTable.setSortingEnabled(True)
        self.removeField.setText(_translate("fieldDialog", "Remove field"))
