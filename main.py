import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700,300, 500, 500)
        self.setWindowIcon(QIcon("1.png"))
        self.button = QPushButton("Click me!", self)
        # self.setFixedSize(500,500)
        self.initUI()

#     def initUI(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)

#         label1 = QLabel("#1", self)
#         label2 = QLabel("#2", self)
#         label3 = QLabel("#3", self)
#         label4 = QLabel("#4", self)
#         label5 = QLabel("#5", self)

#         label1.setStyleSheet("background-color: red;")
#         label2.setStyleSheet("background-color: yellow;")
#         label3.setStyleSheet("background-color: green;")
#         label4.setStyleSheet("background-color: blue;")
#         label5.setStyleSheet("background-color: purple;")

#         # vbox = QVBoxLayout()

#         # vbox.addWidget(label1, 0,0)
#         # vbox.addWidget(label2, 0, 1)
#         # vbox.addWidget(label3, 1, 0)
#         # vbox.addWidget(label4, 1, 1)
#         # vbox.addWidget(label5,1,2)
#         vbox = QGridLayout()

#         vbox.addWidget(label1, 0,0)
#         vbox.addWidget(label2, 0, 1)
#         vbox.addWidget(label3, 1, 0)
#         vbox.addWidget(label4, 1, 1)
#         vbox.addWidget(label5,1,2)

#         central_widget.setLayout(vbox)


# #       ------------labels align------------

#         # label = QLabel("Hello",self)
#         # label.setFont(QFont("Arial", 40))
#         # label.setGeometry(0,0,500,100)
#         # label.setStyleSheet("color: #1d1f24;"
#         #                     "background-color: #7795e0;"
#         #                     "font-weight: bold;"
#         #                     "font-style: italic;"
#         #                     "text-decoration: underline;")
        
#         # label.setAlignment(Qt.AlignTop) Vertically top inside its div
#         # label.setAlignment(Qt.AlignBottom) at bottom 
#         # label.setAlignment(Qt.AlignVCenter) vetical center
#         # label.setAlignment(Qt.AlignRight)
#         # label.setAlignment(Qt.AlignHCenter)
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) center and top
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) center and bottom
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) center and center
#         # label.setAlignment(Qt.AlignCenter) centers both h and v

# #       ------------Images------------
#         # label = QLabel(self)
#         # label.setGeometry(0,0,250,250)

#         # pixmap = QPixmap("1.png")
#         # label.setPixmap(pixmap)

#         # label.setScaledContents(True)

    def initUI(self):
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)


    def on_click(self):
        print("Button Clicked")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()