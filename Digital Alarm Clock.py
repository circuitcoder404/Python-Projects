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

        # Clock Label
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        # Font setup (bold, large size)
        font = QFont("DS-Digital", 80, QFont.Bold)  
        self.label.setFont(font)

        # Styling the label (colors, glow effect)
        self.label.setStyleSheet("""
            QLabel {
                color: #00FF00;                /* Neon green color */
                background-color: black;       /* Dark background */
                border: 2px solid #333;        /* Subtle border */
                padding: 20px;
                border-radius: 15px;           /* Rounded edges */
            }
        """)

        layout.addWidget(self.label)
        self.setLayout(layout)

        # Timer to update every second
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()  # Show immediately
        self.setWindowTitle("Digital Clock")
        self.resize(500, 200)   # Decent size

        # Dark background for the whole window
        self.setStyleSheet("background-color: black;")

    def showTime(self):
        time = QTime.currentTime().toString("hh : mm : ss")
        self.label.setText(time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())







