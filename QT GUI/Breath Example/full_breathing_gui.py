import breath_gui
import pylab
import breath_gui
import multiprocessing
from pylab import *

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)


    def LiveGraph(arg):
        global values, threshold
        xaxis = pylab.arange(len(values)-100, len(values),1)
        line1[0].set_data(xaxis, pylab.array(values[-100:]))
        line2[0].set_data(xaxis, threshold)
        ax.axis([xaxis.min(), xaxis.max(), -1.5,1.5])
        manager.canvas.draw()

    def SinwaveformGenerator(arg):
      global values,T1,Konstant,T0, target, savestatus, jobs
      #ohmegaCos=arccos(T1)/Ta
      #print "fcos=", ohmegaCos/(2*pi), "Hz"

      Tnext=((Konstant*T1)*2)-T0
      if len(values)%100>70:
        randnum = random()*2-1
        values.append(randnum)

        
      else:
        values.append(Tnext)


      if savestatus:
            p = multiprocessing.Process(target=write_to_file(Tnext))
            jobs.append(p)
            p.start()
            
      T0=T1
      T1=Tnext

    def graphstart(arg):
        fig.show()
        global timer1, timer2
        timer.start()
        timer2.start()
        pylab.show()

    def stop_plot(arg):
        global timer, timer2
        timer.stop()
        timer2.stop()

    def set_threshold(arg):
        global threshold
        threshold = float(uiplot.lineEdit_manual_thresh.text())

    def begin_saving(arg):
        global filename, savestatus
        savestatus = 1
        if uiplot.lineEdit_save_file.text() !=  "":
            filename = uiplot.lineEdit_save_file.text()
        tosave = open(filename, 'w')
        filename = tosave

    def write_to_file(data):
        global filename
        filename.write(str(data))
        filename.write("\n")
        
        
        
    #Set the window from imported breath_gui
    gui_plot = breath_gui.QtWidgets.QMainWindow()
    uiplot = breath_gui.Ui_MainWindow()
    uiplot.setupUi(gui_plot)

    #Set graph to start
    xAchse=pylab.arange(0,100,1)
    yAchse=pylab.array([0]*100)

    fig = pylab.figure(1)
    ax = fig.add_subplot(111)
    ax.grid(True)
    ax.set_title("Realtime Randomized Sinusoid")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.axis([0,100,-1.5,1.5])
    line1=ax.plot(xAchse,yAchse,'-', linewidth=2)
    line2=ax.plot(xAchse,yAchse,'-')
    setp(line2, linewidth=2, color='r')

    manager = pylab.get_current_fig_manager()

    values=[]
    values = [0 for x in range(100)]
    
    threshold = 1.5
    Ta=0.01
    fa=1.0/Ta
    fcos=3.5
    Konstant=cos(2*pi*fcos*Ta)
    T0=1.0
    T1=Konstant

    filename = "sessionData.txt"
    savestatus=0
    jobs = []
    
    
    #Set buttons
    uiplot.pushButton_livePlot.clicked.connect(graphstart)
    uiplot.pushButton_stopTracking.clicked.connect(stop_plot)
    uiplot.pushButton_setManual.clicked.connect(set_threshold)
    tosave = uiplot.save_checkbox.clicked.connect(begin_saving) 


    #Set Timers
    timer=fig.canvas.new_timer(interval=20)
    timer.add_callback(LiveGraph, ())
    timer2 = fig.canvas.new_timer(interval=20)
    timer2.add_callback(SinwaveformGenerator, ())
    
    gui_plot.show()
    sys.exit(app.exec_())
