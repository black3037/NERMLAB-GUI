"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

$$\      $$\  $$$$$$\ $$$$$$$$\  $$$$$$\  $$$$$$$\  $$\        $$$$$$\  $$$$$$$\  
$$$\    $$$ |$$  __$$\\__$$  __|$$  __$$\ $$  __$$\ $$ |      $$  __$$\ $$  __$$\ 
$$$$\  $$$$ |$$ /  $$ |  $$ |   $$ /  $$ |$$ |  $$ |$$ |      $$ /  $$ |$$ |  $$ |
$$\$$\$$ $$ |$$ |  $$ |  $$ |   $$ |  $$ |$$$$$$$  |$$ |      $$$$$$$$ |$$$$$$$\ |
$$ \$$$  $$ |$$ |  $$ |  $$ |   $$ |  $$ |$$  __$$< $$ |      $$  __$$ |$$  __$$\ 
$$ |\$  /$$ |$$ |  $$ |  $$ |   $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |
$$ | \_/ $$ | $$$$$$  |  $$ |    $$$$$$  |$$ |  $$ |$$$$$$$$\ $$ |  $$ |$$$$$$$  |
\__|     \__| \______/   \__|    \______/ \__|  \__|\________|\__|  \__|\_______/ 
                                                                                                                                
MotorLab (c)
Kansas State University
Developers: Derek Black
MIT Open License
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
List of files needed to be linked:

Start File  MotorLab.py

Linked      MotorLab_Ui.py
            MotorLabmainWindow.py
            plot_tools.py
            SerialCommunication.py
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   
"""
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMPORTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from PyQt4.QtGui import QApplication, QSplashScreen, QPixmap

import sys
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
""" 


Start up the GUI                                                               
       
                                                                           
"""
# Get randomly generated temporary path set by executable
if __name__ == "__main__":
    
    if getattr(sys, 'frozen', None):
        
        basedir = sys._MEIPASS
        
    else:
        
        import os
        
        basedir = os.path.dirname(__file__)
    

    # Create and display the splash screen
    directory_to_image = str(basedir) + '\Data\splash_loading.png'
    splashme = QApplication(sys.argv)
    splash_pix = QPixmap(directory_to_image)
    splash = QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    splash.show()
    splashme.processEvents()
    
    import time
    time.sleep(3)
    
    app = QApplication(sys.argv)
    
    # Give GUI a theme
    # Some look better than others on different operating systems
    # That is why I choose not to use a single style
    if sys.platform == 'win32':
        
        app.setStyle('cleanlooks')
        
    elif sys.platform == 'darwin':
        
        app.setStyle('mac')
        
    elif sys.platform == 'linux2':
        
        app.setStyle('cleanlooks')
    
    else: 
        
        app.setStyle('cleanlooks')
        
    from MotorLabMainWindow import MotorLabMainWindow      
    window = MotorLabMainWindow() # Create instance of Motor Main Window Class
    window.show()                 # Show the GUI to the end user
    splash.finish(window)         # Terminate splash after GUI is loaded
    sys.exit(app.exec_())         # Exit
