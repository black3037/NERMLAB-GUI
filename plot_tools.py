"""

Simple plotting tools for the MotorLab GUI


"""
# ********************************IMPORTS************************************#
# ***************************************************************************#
from PyQt4.QtGui import QMainWindow

from MotorLab_Ui import Ui_Motorlab

import matplotlib.pyplot as plt

from scipy import signal

from LinearRegression import LinearRegression
# ***************************************************************************#
# ***************************************************************************#

class plot_tools(QMainWindow, Ui_Motorlab):
    def __init__(self):        
        QMainWindow.__init__(self)
        self.setupUi(self)
        
    def bode(self,num,den):
        
        w, mag, phase = signal.bode((num,den))
        
        constant_line_gain = [0]*w
        
        plt.figure("Bode")
        plt.ion()
        f, axarr = plt.subplots(2, sharex=True)
        plt.subplot(211)
        plt.semilogx(w,mag,'dodgerblue')
        plt.semilogx(w,constant_line_gain,color='grey',linestyle='-.')
        plt.title('Bode Diagram')
        plt.ylabel('Magnitude (dB)')
        plt.subplot(212)
        plt.semilogx(w, phase,'dodgerblue')
        plt.ylabel('Phase (Deg)')
        plt.xlabel('Frequency (rad/s)')
        
        return plt.show()
    
    def bode2(self,num,den):
        
        w, mag, phase = signal.bode((num,den))
        
        
        plt.figure("Bode")
        plt.ion()
        plt.rc('font', family='serif')
        plt.rc('xtick', labelsize='x-small')
        plt.rc('ytick', labelsize='x-small')    
        f, axarr = plt.subplots(2, sharex=True)
        plt.subplot(211)
        plt.semilogx(w,mag,'black',label='OL TF')
        plt.legend(loc='upper right')
        plt.title('Bode Diagram')
        plt.ylabel('Magnitude (dB)')
        plt.grid(True, which="both")
        plt.subplot(212)
        plt.semilogx(w, phase,'black',label='Phase')  
        plt.ylabel('Phase (Deg)')
        plt.xlabel('Frequency (rad/s)')
        plt.grid(True,which="both")
        
        return plt.show()
        
    def plotdata(self,*argv):
        
        x,y = argv[0],argv[1]
        plt.scatter(y,x)
        return plt.show()
        
    def fitdata(self,*argv):
        
        x,y = argv[0],argv[1]
        [x1,x2] = LinearRegression(x,y)
                
        y_fit = []
        for fit in y:
            y_fit.append( x1 + x2*fit )    
            
        plt.scatter(y,x)
        plt.plot(y_fit,x)
        return plt.show()
        
    def plotcompare(self,*argv):
        
        return plt.show()
    
    def stepmodel(self,num,den):
                
        t, y = signal.step2((num,den))
        
        #TODO: Note this messes up for unstable or oscillatory systems
        get_last_value = y[-1]
        dcgain = [get_last_value]*len(t)
        upper_limit_error = get_last_value + 0.02 * get_last_value
        lower_limit_error = get_last_value - 0.02 * get_last_value
      
        plt.figure("Step Response")
        plt.ion()
        plt.plot(t,y,'dodgerblue',t,dcgain,'k:')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.title('Step Response')
        
        return plt.show()
            
    def stepmodel2(self,num,den):
        
        t, y = signal.step2((num,den))
        
        #TODO: Note this messes up for unstable or oscillatory systems
        get_last_value = y[-1]
        dcgain = [get_last_value]*len(t)
        upper_limit_error = get_last_value + 0.02 * get_last_value
        lower_limit_error = get_last_value - 0.02 * get_last_value

        plt.figure("Step Response")  
        plt.ion()
        plt.rc('font', family='serif')
        plt.rc('xtick', labelsize='x-small')
        plt.rc('ytick', labelsize='x-small')     
        plt.plot(t,y,'black',label='Model')
        plt.plot(t,dcgain,'k:',label='Command')
        plt.fill_between(t,y,dcgain,color='lightgrey',alpha=0.3)
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.title('Step Response')
        plt.legend(loc='lower right')
        
        return plt.show()
          