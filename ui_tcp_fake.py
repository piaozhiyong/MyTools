# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tcp_fake.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tcp_Dialog(object):
    def setupUi(self, tcp_Dialog):
        tcp_Dialog.setObjectName("tcp_Dialog")
        tcp_Dialog.resize(300, 300)
        self.label = QtWidgets.QLabel(tcp_Dialog)
        self.label.setGeometry(QtCore.QRect(10, 9, 111, 16))
        self.label.setObjectName("label")
        self.lineEdit_ipaddress = QtWidgets.QLineEdit(tcp_Dialog)
        self.lineEdit_ipaddress.setGeometry(QtCore.QRect(50, 40, 133, 20))
        self.lineEdit_ipaddress.setObjectName("lineEdit_ipaddress")
        self.label_3 = QtWidgets.QLabel(tcp_Dialog)
        self.label_3.setGeometry(QtCore.QRect(8, 70, 36, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(tcp_Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 140, 171, 121))
        self.textEdit.setObjectName("textEdit")
        self.pBtn_connectserver = QtWidgets.QPushButton(tcp_Dialog)
        self.pBtn_connectserver.setGeometry(QtCore.QRect(190, 50, 75, 41))
        self.pBtn_connectserver.setObjectName("pBtn_connectserver")
        self.pBtn_send = QtWidgets.QPushButton(tcp_Dialog)
        self.pBtn_send.setGeometry(QtCore.QRect(190, 140, 75, 51))
        self.pBtn_send.setObjectName("pBtn_send")
        self.label_4 = QtWidgets.QLabel(tcp_Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(tcp_Dialog)
        self.label_2.setGeometry(QtCore.QRect(8, 40, 36, 16))
        self.label_2.setObjectName("label_2")
        self.label_sendstatu = QtWidgets.QLabel(tcp_Dialog)
        self.label_sendstatu.setGeometry(QtCore.QRect(10, 270, 171, 16))
        self.label_sendstatu.setText("")
        self.label_sendstatu.setObjectName("label_sendstatu")
        self.lineEdit_port = QtWidgets.QLineEdit(tcp_Dialog)
        self.lineEdit_port.setGeometry(QtCore.QRect(50, 70, 133, 20))
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.label_connectstatu = QtWidgets.QLabel(tcp_Dialog)
        self.label_connectstatu.setGeometry(QtCore.QRect(10, 100, 171, 16))
        self.label_connectstatu.setText("")
        self.label_connectstatu.setObjectName("label_connectstatu")

        self.retranslateUi(tcp_Dialog)
        QtCore.QMetaObject.connectSlotsByName(tcp_Dialog)

    def retranslateUi(self, tcp_Dialog):
        _translate = QtCore.QCoreApplication.translate
        tcp_Dialog.setWindowTitle(_translate("tcp_Dialog", "TCP Fake"))
        self.label.setText(_translate("tcp_Dialog", "1.连接TCP服务端"))
        self.lineEdit_ipaddress.setText(_translate("tcp_Dialog", "127.0.0.1"))
        self.label_3.setText(_translate("tcp_Dialog", "端口号"))
        self.pBtn_connectserver.setText(_translate("tcp_Dialog", "连接"))
        self.pBtn_send.setText(_translate("tcp_Dialog", "发送"))
        self.label_4.setText(_translate("tcp_Dialog", "2.发送消息"))
        self.label_2.setText(_translate("tcp_Dialog", "IP地址"))
        self.lineEdit_port.setText(_translate("tcp_Dialog", "8080"))

