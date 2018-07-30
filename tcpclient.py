#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2018 Wudr. All Rights Reserved.
#
#
# https://github.com/camppolite/MyTools
# ==============================================================================

import socket
import sys
import json
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSlot
from ui_tcpclient import Ui_tcpclient_Dialog


class TCPfake(QDialog):

    def __init__(self):
        super().__init__()

        self.ui_tcpcli = Ui_tcpclient_Dialog()
        self.ui_tcpcli.setupUi(self)
        self.ui_tcpcli.pBtn_break.setDisabled(True)
        self.ui_tcpcli.pBtn_connectserver.setDisabled(True)
        self.sock = None
        # 绑定信号槽
        self.bindsignal()

    def bindsignal(self):
        """绑定信号槽"""
        self.ui_tcpcli.pBtn_connectserver.clicked.connect(self.connecttcpserver)
        self.ui_tcpcli.pBtn_break.clicked.connect(self.shutdowntcp)
        self.ui_tcpcli.pBtn_send.clicked.connect(self.sendmessage)

    @pyqtSlot()
    def connecttcpserver(self):
        """连接TCP服务端,目前没有什么用途"""
        self.ui_tcpcli.label_connectstatu.setText("连接服务端...")
        host = self.ui_tcpcli.lineEdit_ipaddress.text()
        prot = self.ui_tcpcli.lineEdit_port.text()
        address = (host, int(prot))
        # Create a socket (SOCK_STREAM means a TCP socket)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置超时时间，以秒为单位
        self.sock.settimeout(10)
        try:
            self.sock.connect(address)
            self.ui_tcpcli.label_connectstatu.setText("已连接...")
            self.ui_tcpcli.pBtn_connectserver.setDisabled(True)
            self.ui_tcpcli.pBtn_break.setDisabled(False)
            self.ui_tcpcli.pBtn_break.setFocus()
        except socket.timeout as e:
            m_box = QMessageBox(parent=self)
            m_box.setWindowTitle("提示")
            m_box.setText("连接：" + str(e))
            m_box.exec_()
            return

        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()

    @pyqtSlot()
    def shutdowntcp(self):
        """
        使用shutdown来关闭socket的功能
        SHUT_RDWR：关闭读写，即不能使用send/write/recv/read等
        SHUT_RD：关闭读，即不能使用read/recv等
        SHUT_WR:关闭写功能，即不能使用send/write等
        除此之外，还将缓冲区中的内容清空
        """
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()

        self.ui_tcpcli.label_connectstatu.clear()
        self.ui_tcpcli.pBtn_break.setDisabled(True)
        self.ui_tcpcli.pBtn_connectserver.setDisabled(False)
        self.ui_tcpcli.pBtn_connectserver.setFocus()

    @pyqtSlot()
    def sendmessage(self):
        """发送TCP消息"""
        data = self.ui_tcpcli.textEdit.toPlainText()
        if not data:
            return
        # 将 Python 对象编码成 JSON 字符串
        data = json.dumps(data, ensure_ascii=False)

        timeout = self.ui_tcpcli.lineEdit_timeout.text()
        host = self.ui_tcpcli.lineEdit_ipaddress.text()
        prot = self.ui_tcpcli.lineEdit_port.text()
        address = (host, int(prot))
        # Create a socket (SOCK_STREAM means a TCP socket)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置超时时间，以秒为单位
        self.sock.settimeout(int(timeout))
        try:
            self.sock.connect(address)
            self.sock.sendall(bytes(data + "\n", "utf-8"))
            # Receive data from the server and shut down
            received = str(self.sock.recv(1024), "utf-8")
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
            # 在控件上显示服务器返回的消息
            self.ui_tcpcli.textBrowser.setText(received)
        except socket.timeout as e:
            m_box = QMessageBox(parent=self)
            m_box.setWindowTitle("提示")
            m_box.setText("接收：" + str(e))
            m_box.exec_()
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tcpf = TCPfake()
    tcpf.show()
    sys.exit(app.exec_())
