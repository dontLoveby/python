import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont

class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.WINSOW_WIDTH = 800
        self.WINSOW_HEIGHT = 600
        self.foutsize = 18
        self.operating = (
'''    移动：
    |   使用“上”,“下”,“左”,“右”或使用鼠标点击角色周围进
    |   行移动操作；
    交互：
    |   点击交互(或交谈、交换、购买、打开等)按钮或点击
    |   角色周围可交互的物体；
''')
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.update_widgets)
        self.timer2.start(50) 
        #print(self.disW(300), self.width())
        self.setWindowTitle("生存小游戏")
        self.setGeometry(50, 50, self.WINSOW_WIDTH, self.WINSOW_HEIGHT)

        self.label1 = QLabel("进入文字世界？", self)
        self.label1.setGeometry(self.disW(100), self.disH(100), self.disW(600), self.disH(60))
        self.label2 = QLabel("操作说明：", self)
        self.label2.setGeometry(self.disW(0), self.disH(0), self.disW(600), self.disH(500))
        self.label2.hide()

        self.button1 = QPushButton("是的!", self)
        self.button1.setGeometry(self.disW(300), self.disH(400), self.disW(200), self.disH(60))
        self.button1.clicked.connect(self.handle_button1_click)
        self.button2 = QPushButton("探索", self)
        self.button2.setGeometry(self.disW(220), self.disH(480), self.disW(120), self.disH(40))
        #self.button2.clicked.connect(self.handle_button1_click)
        self.button2.hide()
############################################一些计算函数############################################
    def disF(self, size):
        return round(size/(self.WINSOW_WIDTH*round(self.WINSOW_HEIGHT*0.7))*self.width()*self.height())
    def disW(self, width):
        return round(width/self.WINSOW_WIDTH*self.width())
    
    def disH(self, height):
        return round(height/self.WINSOW_HEIGHT*self.height())

    def handle_button1_click(self):
        self.label1.setText("准备好进入文字世界了吗？")
        self.button1.setText("准备好了!")
        self.button1.clicked.connect(self.enter_world)
############################################处理键盘事件############################################
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
############################################处理游戏事件############################################
    """'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
    def enter_world(self):
        self.label1.setText("进入文字世界")
        self.button2.show()
        self.button1.setText("操作说明")
        self.button1.setGeometry(self.disW(50), self.disH(480), self.disW(160), self.disH(80))
        self.button1.clicked.connect(self.operating_instruction)
    
    def operating_instruction(self):#操作说明
        self.current_operating = ""
        self.operating_index = 0
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.update_operating)
        self.timer1.start(40)  # 设置延迟时间为100毫秒
        self.label2.show()
        self.label1.hide()
        # 将timer对象设置为self的属性
        #self.timer.setObjectName("timer")
        self.button1.setText("我明白了")
        self.button1.clicked.connect(self.no_operating_instruction)

    def update_operating(self):
        if (self.operating_index < len(self.operating)): 
            self.current_operating += self.operating[self.operating_index]
            if (self.operating[self.operating_index] != ' ' and self.operating[self.operating_index] != ' '):
                #print("操作说明：\n"+self.operating[:self.operating_index+1])#调试
                self.label2.setGeometry(self.disW(10), self.disH(7.5), self.disW(600), self.disH(500))
                self.label2.setText("操作说明：\n" + self.current_operating)
                self.label2.adjustSize()
            self.operating_index += 1
        else:
            self.timer1.stop()

    def update_widgets(self):#更新部分组件状态
        font = QFont("Arial", self.disF(self.foutsize))  # 创建一个字体对象，设置字体为Arial，大小为12
        self.label1.setFont(font)
        self.label2.setFont(font)
        self.button2.setGeometry(self.disW(220), self.disH(480), self.disW(120), self.disH(40))
        if self.button1.text() == "操作说明" or self.button1.text() == "我明白了":
            self.button1.setGeometry(self.disW(50), self.disH(480), self.disW(160), self.disH(80))
        else:
            self.button1.setGeometry(self.disW(300), self.disH(400), self.disW(200), self.disH(60))

    def no_operating_instruction(self):
        self.operating_index = len(self.operating)
        self.button1.setText("操作说明")
        font = QFont("Arial", self.disF(self.foutsize))  # 创建一个字体对象，设置字体为Arial，大小为disF(12)
        self.label1.setFont(font)
        self.label2.setFont(font)
        self.label2.hide()
        self.label1.show()
        self.button1.clicked.connect(self.operating_instruction)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())

