# ============== File Dialog ================
# ===== Button / Label / Graph vertical setting =====
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc
from pathlib import Path
import sys


class MyApp(QWidget) :
    def __init__(self) :
        super().__init__()
        self.initUI()
        
    def initUI(self) :
        
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()         # we need 2 lines for using HANGEUL
        rc('font', family=font_name)
        
        
        layout = QVBoxLayout()
        
        
        
        # ========== layoutTop ===========
        layoutTop = QHBoxLayout()
        self.btnImg = QPushButton('이미지 불러오기')
        self.btnImg.clicked.connect(self.btnImageHandler)
        layout.addWidget(self.btnImg)
        
        
        # ========= layoutImg ==========
        layoutImg = QVBoxLayout()
        self.lblImg = QLabel('')
        layout.addWidget(self.lblImg)
        
        
        # ========= layoutGraph ==========
        layoutGraph = QVBoxLayout()
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
        
        
        # ========== main Window setting ===========
        self.setLayout(layout)
        self.setWindowTitle('QFileDialog + LoadImg')
        self.setGeometry(10, 30, 500, 650)
        self.show()
        
        
        layout.addLayout(layoutTop)
        layout.addLayout(layoutImg)
        layout.addLayout(layoutGraph)
        
        
        # ===== structure_1 : load image directly =====
    def btnImageHandler(self) :
        
        home_dir = str(Path.home())
        # QMessageBox.about(self, 'title', home_dir)                          # using a lot for debugging
        self.OpenFile = QFileDialog.getOpenFileName(self, '이미지열기', directory=home_dir, filter='Images (*.png, *.jpg)')
        self.lblImg.setPixmap(QPixmap(self.OpenFile[0]))
        self.graph()
    
        # ===== structure_2 : load image by matplotlib =====
    def graph(self) :
        
        self.fig.clear()                                                    # 그래프 영역 초기화
        ax = self.fig.add_subplot(111)                                      # 그래프 영역 1개일 경우
        ax.clear()                                                          # 그래프 영역 초기화(subplot 각각 필요)
        img = mpimg.imread(self.OpenFile[0])
        ax.xticks([])
        ax.yticks([])
        ax.imshow(img)
        
        self.canvas.draw()                                                  # 그래프 다시 그리기
        
        
        
        
        
    
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    
    