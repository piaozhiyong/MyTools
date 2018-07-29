#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2018 Wudr. All Rights Reserved.
#
#
# https://github.com/camppolite/MyTools
# ==============================================================================

import socket
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSlot
from ui_tcp_fake import Ui_tcp_Dialog


class TCPfake(QDialog):

    def __init__(self):
        super().__init__()

        self.ui_tcp = Ui_tcp_Dialog()
        self.ui_tcp.setupUi(self)
        self.bindsignal()

    def bindsignal(self):
        """绑定信号槽"""
        self.ui_tcp.pBtn_connectserver.clicked.connect(self.connecttcpserver)
        self.ui_tcp.pBtn_send.clicked.connect(self.sendmessage)

    @pyqtSlot()
    def connecttcpserver(self):
        self.ui_tcp.label_connectstatu.setText("连接服务端")
        host = self.ui_tcp.lineEdit_ipaddress.text()
        prot = self.ui_tcp.lineEdit_port.text()
        address = (host, int(prot))
        # Create a socket (SOCK_STREAM means a TCP socket)
        print(type(host))
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(address)

    @pyqtSlot()
    def sendmessage(self):
        self.ui_tcp.label_sendstatu.setText("发送消息")
        data = self.ui_tcp.textEdit.toPlainText()
        self.sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(self.sock.recv(1024), "utf-8")

        print("Sent:     {}".format(data))
        print("Received: {}".format(received))
        # while True:
        #     m_data = input(">")
        #     if not m_data:
        #         break
        #     sock.send(m_data.encode())
        #     m_data = sock.recv(BUFFSIZE).decode()
        #     if not m_data:
        #         break
        #     print(m_data)
        # sock.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tcpf = TCPfake()
    tcpf.show()
    sys.exit(app.exec_())
