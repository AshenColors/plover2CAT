# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plover_cat\affix_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_affixDialog(object):
    def setupUi(self, affixDialog):
        affixDialog.setObjectName("affixDialog")
        affixDialog.resize(387, 173)
        self.verticalLayout = QtWidgets.QVBoxLayout(affixDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(affixDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.styleName = QtWidgets.QComboBox(affixDialog)
        self.styleName.setObjectName("styleName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.styleName)
        self.line = QtWidgets.QFrame(affixDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line)
        self.label_3 = QtWidgets.QLabel(affixDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.prefixString = QtWidgets.QLineEdit(affixDialog)
        self.prefixString.setClearButtonEnabled(False)
        self.prefixString.setObjectName("prefixString")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.prefixString)
        self.label_2 = QtWidgets.QLabel(affixDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.suffixString = QtWidgets.QLineEdit(affixDialog)
        self.suffixString.setObjectName("suffixString")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.suffixString)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.insertTab = QtWidgets.QPushButton(affixDialog)
        self.insertTab.setFocusPolicy(QtCore.Qt.NoFocus)
        self.insertTab.setObjectName("insertTab")
        self.horizontalLayout.addWidget(self.insertTab)
        self.saveAffixes = QtWidgets.QPushButton(affixDialog)
        self.saveAffixes.setObjectName("saveAffixes")
        self.horizontalLayout.addWidget(self.saveAffixes)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.affixButtonBox = QtWidgets.QDialogButtonBox(affixDialog)
        self.affixButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.affixButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.affixButtonBox.setObjectName("affixButtonBox")
        self.verticalLayout.addWidget(self.affixButtonBox)

        self.retranslateUi(affixDialog)
        self.affixButtonBox.accepted.connect(affixDialog.accept) # type: ignore
        self.affixButtonBox.rejected.connect(affixDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(affixDialog)

    def retranslateUi(self, affixDialog):
        _translate = QtCore.QCoreApplication.translate
        affixDialog.setWindowTitle(_translate("affixDialog", "Dialog"))
        self.label.setText(_translate("affixDialog", "Style:"))
        self.label_3.setText(_translate("affixDialog", "Prefix string:"))
        self.label_2.setText(_translate("affixDialog", "Suffix string:"))
        self.insertTab.setText(_translate("affixDialog", "Insert tab at cursor"))
        self.saveAffixes.setText(_translate("affixDialog", "Save"))
