from gui import Ui_jarvisui
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import maincode
import sys


class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        maincode.Taskexecution()


startexecution = MainThread()


class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui = Ui_jarvisui()
        self.gui.setupUi(self)

        self.gui.push_START.clicked.connect(self.startTask)
        self.gui.push_Quit.clicked.connect(self.close)

    def startTask(self):

        self.gui.label1 = QtGui.QMovie(
            "..//jarvis ui gif//B.G//Iron_Template_1.gif")
        self.gui.gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("..//jarvis ui gif//ExtraGui//live.gif")
        self.gui.gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("..//jarvis ui gif//VoiceReg//__1.gif")
        self.gui.gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("..//jarvis ui gif//8FLR.gif")
        self.gui.gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()

        self.gui.label5 = QtGui.QMovie("..//jarvis ui gif//T8bahf (1).gif")
        self.gui.gif_5.setMovie(self.gui.label5)
        self.gui.label5.start()

        self.gui.label6 = QtGui.QMovie(
            "..//jarvis ui gif//ExtraGui//932fd00d9b43753061c47739f0cc777b.gif")
        self.gui.gif_6.setMovie(self.gui.label6)
        self.gui.label6.start()

        self.gui.label7 = QtGui.QMovie(
            "C://Users//pravi//Desktop/jarvis ui gif/ExtraGui/Code_Template.gif")
        self.gui.gif_7.setMovie(self.gui.label7)
        self.gui.label7.start()

        self.gui.label8 = QtGui.QMovie(
            "C://Users//pravi//Desktop/jarvis ui gif/ExtraGui/dec7zp0-b1f90b09-8dd0-4877-9be1-cf990bad3309.gif")
        self.gui.gif_8.setMovie(self.gui.label8)
        self.gui.label8.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)

        startexecution.start()

    def showTimeLive(self):
        t_time = QTime.currentTime()
        time = t_time.toString()
        d_ate = QDate.currentDate()
        date = d_ate.toString()
        lable_time = "Time :" + time
        label_date = "Date :" + date

        self.gui.time.setText(lable_time)
        self.gui.date_.setText(label_date)


GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())
