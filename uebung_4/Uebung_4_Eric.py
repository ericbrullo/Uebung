import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

        ## Menu Barra
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)
        filemenu.addAction(save)
        filemenu.addAction(quit)

    # schermata testo
    def menu_save(self):
        widgets = self.centralWidget().layout()
        data = {
            "Vorname": widgets.itemAt(1).widget().text(),
            "Name": widgets.itemAt(3).widget().text(),
            "Geburtstag": widgets.itemAt(5).widget().date().toString("dd MM yyyy"),
            "Adresse": widgets.itemAt(7).widget().text(),
            "Postleitzahl": widgets.itemAt(9).widget().text(),
            "Ort": widgets.itemAt(11).widget().text(),
            "Land": widgets.itemAt(13).widget().currentText()
        }
 
        with open("./test.txt", "a") as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")
 
        QMessageBox.information(self, "Saved", "Data has been saved to output.txt")

    def menu_quit(self):
        print("Quit")
        self.close()
        

    ##Permette di creare la finestra
    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("Mein erste GUI")
        
        ### LAYOUT WÄHLEN:
        layout = QFormLayout()
        self.setMinimumSize(500, 250)

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        
        ## Widgets erstellen
        VornameLineEdit = QLineEdit()
        NachnameLineEdit = QLineEdit()
        GeburtstagDateEdit = QDateEdit()
        AdresseLineEdit = QLineEdit()
        PostLeitzhalLineEdit = QLineEdit()
        OrtLineEdit = QLineEdit()
        LandEdit = QComboBox()
        BottonSave = QPushButton("Save")
        BottonSave.clicked.connect(self.menu_save)

        #item in ComboBox
        LandEdit.addItem("Schweiz")
        LandEdit.addItem("Deutschland")
        LandEdit.addItem("Italien")
        LandEdit.addItem("Andere")

        ## Layout füllen
        layout.addRow("Vorname:" , VornameLineEdit)
        layout.addRow("Nachname:" , NachnameLineEdit)
        layout.addRow("Geburtstag:" , GeburtstagDateEdit)
        layout.addRow("Adresse:" , AdresseLineEdit)
        layout.addRow("Postleizhal:" , PostLeitzhalLineEdit)
        layout.addRow("Ort:" , OrtLineEdit)
        layout.addRow("Land:", LandEdit)
        layout.addRow(BottonSave)


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