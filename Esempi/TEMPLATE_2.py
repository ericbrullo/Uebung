import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

##Permette di creare la finestra
    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("Mein erste GUI")
        ### LAYOUT WÄHLEN:
        layout = QGridLayout()

        label = QLabel("Hello")
        edit = QLineEdit()
        button = QPushButton("ok")
        layout.addWidget(label)
        layout.addWidget(edit)
        layout.addWidget(button)

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        
        ## Widgets erstellen
        # ...

        ## Layout füllen
        # ...

        ## Fenster anzeigen
        self.show()


    def createConnects(self):
        pass




def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()