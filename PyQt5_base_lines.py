############## PyQt5 base lines ##############
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MyApp(QWidget) :  
    def __init__(self) :
        super().__init__()  
        self.initUI()
        
    def initUI(self) :
        # ======== if you need to use HANGEUL =========
        # font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        # rc('font', family=font_name)










if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp() 
    sys.exit(app.exec_())