import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
       # self.createConnects()

##Permette di creare la finestra
    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("Mein erste GUI")
        ### LAYOUT WÄHLEN:
        layout = QFormLayout()

        nameLineEdit = QLineEdit()
        emailLineEdit = QLineEdit()
        ageSpinBox = QSpinBox()
        layout.addRow("name:" , nameLineEdit)
        layout.addRow("Email:" , emailLineEdit)
        layout.addRow("Age:" , ageSpinBox)


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