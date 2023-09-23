

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisui(object):
    def setupUi(self, jarvisui):
        jarvisui.setObjectName("jarvisui")
        jarvisui.resize(3200, 1801)
        self.centralwidget = QtWidgets.QWidget(jarvisui)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_0 = QtWidgets.QLabel(self.centralwidget)
        self.bg_0.setGeometry(QtCore.QRect(-20, -90, 3221, 1891))
        self.bg_0.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.bg_0.setText("")
        self.bg_0.setScaledContents(False)
        self.bg_0.setObjectName("bg_0")
        self.bg_1 = QtWidgets.QLabel(self.centralwidget)
        self.bg_1.setGeometry(QtCore.QRect(10, 10, 661, 481))
        self.bg_1.setStyleSheet("background-color: rgb(12, 215, 255);")
        self.bg_1.setText("")
        self.bg_1.setScaledContents(True)
        self.bg_1.setObjectName("bg_1")
        self.bg_2 = QtWidgets.QLabel(self.centralwidget)
        self.bg_2.setGeometry(QtCore.QRect(840, 20, 891, 471))
        self.bg_2.setStyleSheet("background-color: rgb(12, 215, 255);")
        self.bg_2.setText("")
        self.bg_2.setObjectName("bg_2")
        self.gif_1 = QtWidgets.QLabel(self.centralwidget)
        self.gif_1.setGeometry(QtCore.QRect(20, 20, 641, 461))
        self.gif_1.setText("")
        self.gif_1.setPixmap(QtGui.QPixmap(
            "C://Users//pravi//Desktop/jarvis ui gif/B.G/Iron_Template_1.gif"))
        self.gif_1.setScaledContents(True)
        self.gif_1.setObjectName("gif_1")
        self.gif_2 = QtWidgets.QLabel(self.centralwidget)
        self.gif_2.setGeometry(QtCore.QRect(850, 30, 871, 451))
        self.gif_2.setText("")
        self.gif_2.setPixmap(QtGui.QPixmap(
            "C://Users//pravi//Desktop/jarvis ui gif/ExtraGui/live.gif"))
        self.gif_2.setScaledContents(True)
        self.gif_2.setObjectName("gif_2")
        self.gif_3 = QtWidgets.QLabel(self.centralwidget)
        self.gif_3.setGeometry(QtCore.QRect(-70, 1250, 681, 551))
        self.gif_3.setText("")
        self.gif_3.setPixmap(QtGui.QPixmap(
            "C://Users//pravi//Desktop/jarvis ui gif/VoiceReg/__1.gif"))
        self.gif_3.setScaledContents(True)
        self.gif_3.setObjectName("gif_3")
        self.gif_4 = QtWidgets.QLabel(self.centralwidget)
        self.gif_4.setGeometry(QtCore.QRect(710, 600, 1471, 891))
        self.gif_4.setText("")
        self.gif_4.setPixmap(QtGui.QPixmap(
            "C://Users//pravi//Desktop/jarvis ui gif/8FLR.gif"))
        self.gif_4.setScaledContents(True)
        self.gif_4.setObjectName("gif_4")
        self.gif_5 = QtWidgets.QLabel(self.centralwidget)
        self.gif_5.setGeometry(QtCore.QRect(2510, 20, 681, 281))
        self.gif_5.setText("")
        self.gif_5.setPixmap(QtGui.QPixmap(
            "C://Users//pravi//Desktop/jarvis ui gif/T8bahf (1).gif"))
        self.gif_5.setScaledContents(True)
        self.gif_5.setObjectName("gif_5")
        self.bg_3 = QtWidgets.QLabel(self.centralwidget)
        self.bg_3.setGeometry(QtCore.QRect(2600, 310, 411, 91))
        self.bg_3.setText("")
        self.bg_3.setPixmap(QtGui.QPixmap(
            "C://Users//pravi//Desktop/jarvis ui gif/B.G/wp1913256.jpg"))
        self.bg_3.setScaledContents(True)
        self.bg_3.setObjectName("bg_3")
        self.bg_4 = QtWidgets.QLabel(self.centralwidget)
        self.bg_4.setGeometry(QtCore.QRect(2600, 480, 411, 91))
        self.bg_4.setText("")
        self.bg_4.setPixmap(QtGui.QPixmap(
            "C://Users//pravi//Desktop/jarvis ui gif/B.G/wp1913256.jpg"))
        self.bg_4.setScaledContents(True)
        self.bg_4.setObjectName("bg_4")
        self.date_ = QtWidgets.QTextBrowser(self.centralwidget)
        self.date_.setGeometry(QtCore.QRect(2650, 500, 311, 51))
        self.date_.setStyleSheet("background-color: Transparent;\n"
                                 "border-color:None;\n"
                                 "color: rgb(8, 136, 255);\n"
                                 "")
        self.date_.setObjectName("date_")
        self.time = QtWidgets.QTextBrowser(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(2650, 330, 311, 51))
        self.time.setStyleSheet("background-color: Transparent;\n"
                                "border-color:None;\n"
                                "color: rgb(8, 136, 255);\n"
                                "")
        self.time.setObjectName("time")
        self.push_START = QtWidgets.QPushButton(self.centralwidget)
        self.push_START.setGeometry(QtCore.QRect(2810, 1490, 261, 71))
        self.push_START.setStyleSheet("background-color: TRANSPARENT;\n"
                                      "font: 22pt \"Courier New\";\n"
                                      "\n"
                                      "\n"
                                      "border-color: rgb(33, 255, 241);\n"
                                      "color: rgb(33, 255, 241);\n"
                                      "")
        self.push_START.setObjectName("push_START")
        self.bg_5 = QtWidgets.QLabel(self.centralwidget)
        self.bg_5.setGeometry(QtCore.QRect(2790, 1480, 301, 91))
        self.bg_5.setText("")
        self.bg_5.setPixmap(QtGui.QPixmap(
            "C://Users//pravi//Desktop/jarvis ui gif/Buttons/Start.png"))
        self.bg_5.setScaledContents(True)
        self.bg_5.setObjectName("bg_5")
        self.bg_6 = QtWidgets.QLabel(self.centralwidget)
        self.bg_6.setGeometry(QtCore.QRect(2790, 1610, 311, 81))
        self.bg_6.setText("")
        self.bg_6.setPixmap(QtGui.QPixmap(
            "C://Users//pravi//Desktop/jarvis ui gif/Buttons/Quit.png"))
        self.bg_6.setScaledContents(True)
        self.bg_6.setObjectName("bg_6")
        self.push_Quit = QtWidgets.QPushButton(self.centralwidget)
        self.push_Quit.setGeometry(QtCore.QRect(2820, 1620, 261, 61))
        self.push_Quit.setStyleSheet("background-color: TRANSPARENT;\n"
                                     "font: 20pt \"Courier New\";\n"
                                     "\n"
                                     "\n"
                                     "border-color: rgb(33, 255, 241);\n"
                                     "color: rgb(33, 255, 241);\n"
                                     "")
        self.push_Quit.setObjectName("push_Quit")
        self.gif_6 = QtWidgets.QLabel(self.centralwidget)
        self.gif_6.setGeometry(QtCore.QRect(920, 1580, 1321, 181))
        self.gif_6.setText("")
        self.gif_6.setPixmap(QtGui.QPixmap(
            "C://Users//pravi//Desktop/jarvis ui gif/ExtraGui/932fd00d9b43753061c47739f0cc777b.gif"))
        self.gif_6.setScaledContents(True)
        self.gif_6.setObjectName("gif_6")
        self.gif_7 = QtWidgets.QLabel(self.centralwidget)
        self.gif_7.setGeometry(QtCore.QRect(30, 550, 581, 631))
        self.gif_7.setText("")
        self.gif_7.setPixmap(QtGui.QPixmap(
            "C://Users//pravi//Desktop/jarvis ui gif/ExtraGui/Code_Template.gif"))
        self.gif_7.setScaledContents(True)
        self.gif_7.setObjectName("gif_7")
        self.gif_8 = QtWidgets.QLabel(self.centralwidget)
        self.gif_8.setGeometry(QtCore.QRect(2370, 750, 821, 581))
        self.gif_8.setText("")
        self.gif_8.setPixmap(QtGui.QPixmap(
            "C://Users//pravi//Desktop/jarvis ui gif/ExtraGui/dec7zp0-b1f90b09-8dd0-4877-9be1-cf990bad3309.gif"))
        self.gif_8.setScaledContents(True)
        self.gif_8.setObjectName("gif_8")
        self.bg_0.raise_()
        self.gif_3.raise_()
        self.bg_1.raise_()
        self.bg_2.raise_()
        self.gif_1.raise_()
        self.gif_2.raise_()
        self.gif_4.raise_()
        self.gif_5.raise_()
        self.bg_3.raise_()
        self.bg_4.raise_()
        self.date_.raise_()
        self.time.raise_()
        self.bg_5.raise_()
        self.push_START.raise_()
        self.bg_6.raise_()
        self.push_Quit.raise_()
        self.gif_6.raise_()
        self.gif_7.raise_()
        self.gif_8.raise_()
        jarvisui.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisui)
        QtCore.QMetaObject.connectSlotsByName(jarvisui)

    def retranslateUi(self, jarvisui):
        _translate = QtCore.QCoreApplication.translate
        jarvisui.setWindowTitle(_translate("jarvisui", "MainWindow"))
        self.push_START.setText(_translate("jarvisui", ". . . ."))
        self.push_Quit.setText(_translate("jarvisui", ". . . "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisui = QtWidgets.QMainWindow()
    ui = Ui_jarvisui()
    ui.setupUi(jarvisui)
    jarvisui.show()
    sys.exit(app.exec_())
