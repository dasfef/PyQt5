from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc


class MyApp(QWidget) :
    def __init__(self) :
        super().__init__()
        self.initUI()
        
    def initUI(self) :
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()         # we need 2 lines for using HANGEUL
        rc('font', family=font_name)
        
        
        # ========== layoutTop ===========
        layoutTop = QHBoxLayout()
        self.btnLoad = QPushButton('CSV 불러오기')
        layoutTop.addWidget(self.btnLoad)
        
        # ========== layoutTbl ============
        layoutTbl = QVBoxLayout()
        self.tbl = QTableWidget(0, 7)
        self.col_head = ['Date', 'Temp1', 'Temp2', 'Temp3', 'Temp4', 'Temp5', 'Temp6']
        self.tbl.setHorizontalHeaderLabels(self.col_head)
        layoutTbl.addWidget(self.tbl)
        
        # ========== layoutGraph ===========
        layoutGraph = QVBoxLayout()
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        layoutGraph.addWidget(self.canvas)
        
        
        # ========== representing layout setting ==========
        layout = QVBoxLayout()
        layout.addLayout(layoutTop)
        layout.addLayout(layoutTbl)
        layout.addLayout(layoutGraph)
        
        
        # ========== handler ===========
        self.btnLoad.clicked.connect(self.btnLoadHandler)
        
        
        # ========== main Window setting ===========
        self.setLayout(layout)
        self.setWindowTitle('MyWindow')
        self.setGeometry(650, 30, 800, 650)
        self.show()
    
    
    def btnLoadHandler(self) :
        self.dataProcess()
        self.graph()
        
        
        # ========= dataProcess : open CSV file, set table after save memory ===========   
    def dataProcess(self) :   

        # File Open
        a = QFileDialog.getOpenFileName()
        sensor = pd.read_csv(a[0])
        
        # count and set rows
        csvShape = sensor.shape
        # QMessageBox.about(self, 'title', str(csvShape[0]))
        self.tbl.setRowCount(csvShape[0])
        
        # set variables for draw graph
        self.df = [[0] * 7 for i in range(csvShape[0])]                                     # : 2차원 배열 data append (for 문 한줄 문법)
        
        # set Tables  
        for row in range(0, csvShape[0]) :
            # self.tbl.setItem(row, 0, QTableWidgetItem(sensor.iloc[row, 0]))               # 날짜 시간 문자열
            # df0 = sensor.iloc[row, 0]                                                     # set datas for graph
            for col in range(0, 7) :                                                       
                self.tbl.setItem(row, col, QTableWidgetItem(str(sensor.iloc[row, col])))    # : 행, 열 문자열 변환 후 테이블 삽입
                self.df[row][col] = sensor.iloc[row, col]                                   # : 행, 열 데이터 int 형 데이터 프레임 리스트 추가
                
                # (row, col, QTableWidgetItem(str(sensor.iloc[row, col])))
                # df[row, col] = sensor.iloc[row, col]                                      # set datas for graph
            
        self.graph()
        
                
        # ========= drawing graph ==========
    def graph(self) :
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.clear()
        
        df0 = [k[0] for k in self.df]
        df1 = [k[1] for k in self.df]
        df2 = [k[2] for k in self.df]
        df3 = [k[3] for k in self.df]
        df4 = [k[4] for k in self.df]
        df5 = [k[5] for k in self.df]
        df6 = [k[6] for k in self.df]
        
        ax.plot(df0, df1, 'r--', label = 'temp1')
        ax.plot(df0, df2, 'b-', label = 'temp2')
        ax.plot(df0, df3, 'y-', label = 'temp3')
        ax.plot(df0, df4, 'v:', label = 'temp4')
        ax.plot(df0, df5, 'd-.', label = 'temp5')
        ax.plot(df0, df6, 'g-', label = 'temp6')
        
        ax.legend()
        self.canvas.draw()
        
        
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())