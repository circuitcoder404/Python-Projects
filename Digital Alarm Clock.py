import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()   

    def initUI(self):   
        layout = QVBoxLayout()

        
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        
        font = QFont("DS-Digital", 80, QFont.Bold)  
        self.label.setFont(font)

        
        self.label.setStyleSheet("""
            QLabel {
                color: #00FF00;               
                background-color: black;       
                border: 2px solid #333;       
                padding: 20px;
                border-radius: 15px;           
            }
        """)

        layout.addWidget(self.label)
        self.setLayout(layout)

        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()  
        self.setWindowTitle("Digital Clock")
        self.resize(500, 200)   

        
        self.setStyleSheet("background-color: black;")

    def showTime(self):
        time = QTime.currentTime().toString("hh : mm : ss")
        self.label.setText(time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())







