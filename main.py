import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700,300, 500, 500)
        self.setWindowIcon(QIcon("1.png"))

        label = QLabel("Hello",self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: #1d1f24;"
                            "background-color: #7795e0;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        
        # label.setAlignment(Qt.AlignTop) Vertically top inside its div
        # label.setAlignment(Qt.AlignBottom) at bottom 
        # label.setAlignment(Qt.AlignVCenter) vetical center
        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignHCenter)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) center and top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) center and bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) center and center
        # label.setAlignment(Qt.AlignCenter) centers both h and v


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()