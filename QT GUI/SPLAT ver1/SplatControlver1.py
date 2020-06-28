import SplatAutoGUIver1
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

#========================= GUI Functions=======================================        
    def TestButton(arg):
        if uiplot.TransFile.text() !=  "":
            Translocation = uiplot.TransFile.text()
        if uiplot.RecFile.text() !=  "":
            RecLocation = uiplot.RecFile.text()    
        if uiplot.NoTrans.text() !=  "":
            Transnum = uiplot.NoTrans.text()    
        if uiplot.NoRec.text() !=  "":
            Recnum = uiplot.NoRec.text()                
        print(Translocation)
        print(RecLocation)
        print(Transnum)
        print(Recnum)
        
#========= Shows the Main GUI from the ui file ================================
    gui_screen1 = SplatAutoGUIver1.QtWidgets.QMainWindow()
    uiplot = SplatAutoGUIver1.Ui_MainWindow()
    uiplot.setupUi(gui_screen1)
    
    uiplot.pushButton.clicked.connect(TestButton)
    
    gui_screen1.show()
    sys.exit(app.exec_())