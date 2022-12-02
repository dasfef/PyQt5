from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc
import pymysql


class MyApp(QWidget) :
    def __init__(self) :
        super().__init__()
        self.initUI()
        
    def initUI(self) :
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()         # we need 2 lines for using HANGEUL
        rc('font', family=font_name)
        
        
        layout = QVBoxLayout()
        
        # layoutTop
        layoutTop = QVBoxLayout()
        self.btnLoad = QPushButton('데이터 불러오기')
        self.btnLoad.clicked.connect(self.btnLoadHandler)
        layout.addWidget(self.btnLoad)
        
        
        
        
        
        
        
        
        
        
        
        
    def btnLoadHandler(self) :
        self.dataProcess()
        
        
        
        
        
        
        
        
        
        
        
    def dataProcess(self) :
        #sensor = pd.read_csv()
        conn = pymysql.connect(host = '127.0.0.1', user = 'scott', password = 'tiger', db = 'work', charset = 'utf8')
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
    
    
    
    
    