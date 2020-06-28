
from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_livePlot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_livePlot.setGeometry(QtCore.QRect(50, 270, 241, 141))
        self.pushButton_livePlot.setObjectName(_fromUtf8("pushButton_livePlot"))
        self.save_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.save_checkbox.setGeometry(QtCore.QRect(340, 460, 97, 22))
        self.save_checkbox.setObjectName(_fromUtf8("save_checkbox"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 0, 621, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_manual_thresh = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_manual_thresh.setGeometry(QtCore.QRect(300, 120, 113, 27))
        self.lineEdit_manual_thresh.setText(_fromUtf8(""))
        self.lineEdit_manual_thresh.setObjectName(_fromUtf8("lineEdit_manual_thresh"))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 90, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_setManual = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_setManual.setGeometry(QtCore.QRect(420, 120, 98, 27))
        self.pushButton_setManual.setObjectName(_fromUtf8("pushButton_setManual"))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 160, 71, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_asst = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_asst.setGeometry(QtCore.QRect(300, 190, 221, 27))
        self.pushButton_asst.setObjectName(_fromUtf8("pushButton_asst"))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 460, 271, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_save_file = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_save_file.setGeometry(QtCore.QRect(50, 490, 191, 27))
        self.lineEdit_save_file.setObjectName(_fromUtf8("lineEdit_save_file"))
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 480, 441, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 310, 181, 51))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 510, 291, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton_stopTracking = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stopTracking.setGeometry(QtCore.QRect(520, 300, 161, 71))
        self.pushButton_stopTracking.setObjectName(_fromUtf8("pushButton_stopTracking"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_livePlot.setText(_translate("MainWindow", "Start Live Plot", None))
        self.save_checkbox.setText(_translate("MainWindow", "Yes", None))
        self.label.setText(_translate("MainWindow", "Respiratory System Movement Tracker", None))
        self.label_2.setText(_translate("MainWindow", "Set Threshold Magnitude:", None))
        self.pushButton_setManual.setText(_translate("MainWindow", "Set Manually", None))
        self.label_3.setText(_translate("MainWindow", "OR", None))
        self.pushButton_asst.setText(_translate("MainWindow", "Threshold Assistant", None))
        self.label_4.setText(_translate("MainWindow", "Would you like to save this session\'s data?", None))
        self.label_5.setText(_translate("MainWindow", "Filename to save to (will save in .txt format)", None))
        self.label_6.setText(_translate("MainWindow", "*Opens in a new window", None))
        self.label_7.setText(_translate("MainWindow", "Default filename: sessionData.txt", None))
        self.pushButton_stopTracking.setText(_translate("MainWindow", "Stop Tracking", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

