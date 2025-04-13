import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
       # self.createConnects()

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        editmenu = menubar.addMenu("Edit")
        viewmenu = menubar.addMenu("View")

        open = QAction("Open", self)
        open.triggered.connect(self.menu_open)
        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)

        quit.setMenuRole(QAction.QuitRole)

        filemenu.addAction(open)
        filemenu.addAction(save)
        filemenu.addAction(quit)

    def menu_open(self):
        pass

    def menu_save(save):
        pass

    def menu_quit(self):
        print("Quit")
        self.close()
        

##Permette di creare la finestra
    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("Mein erste GUI")
        ### LAYOUT WÄHLEN:
        layout = QGridLayout()


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