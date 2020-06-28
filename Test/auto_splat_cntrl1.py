import Splat_GUIver2
import sys
import auto_splatver9
from PyQt5 import QtWidgets

#========================= GUI Functions=======================================
global trigger
trigger =0
if __name__ == "__main__" and trigger==0:
    app = QtWidgets.QApplication(sys.argv)

    def TestButton(arg):
        if uiplot.TransFile.text() !=  "":
            Txin = uiplot.TransFile.text()
        if uiplot.RecFile.text() !=  "":
            Rxin = uiplot.RecFile.text()    
        if uiplot.NoTrans.text() !=  "":
            NoTran = int(uiplot.NoTrans.text())    
        if uiplot.NoRec.text() !=  "":
            NoRec = int(uiplot.NoRec.text())                
        if uiplot.NoRec.text() !=  "":
            Transh = uiplot.NoRec_3.text() 
        if uiplot.NoRec.text() !=  "":
            Rech = uiplot.NoRec_4.text() 
        if uiplot.NoRec.text() !=  "":
            Outname = uiplot.NoRec_2.text()    
        gui_screen1.hide()
        auto_splatver9.Automated(Txin, Rxin, NoTran, NoRec, Transh, Rech, Outname)
        quit()

#========= Shows the Main GUI from the ui file ================================
        
    gui_screen1 = Splat_GUIver2.QtWidgets.QMainWindow()
    uiplot = Splat_GUIver2.Ui_MainWindow()
    uiplot.setupUi(gui_screen1)
    uiplot.pushButton.clicked.connect(TestButton)
    gui_screen1.show()
    trigger = 1
    sys.exit(app.exec_())     