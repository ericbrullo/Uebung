import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QDesktopServices
import urllib.parse

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

        ## Menu Barra
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        viewmenu = menubar.addMenu("View")

        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)
        load = QAction("Load", self)  # Nuovo menu per caricare
        load.triggered.connect(self.menu_load)
        map_view = QAction("Karte...", self)  # Menu per la mappa
        map_view.triggered.connect(self.open_google_maps)
        
        filemenu.addAction(save)
        filemenu.addAction(quit)
        filemenu.addAction(load)
        viewmenu.addAction(map_view)

    # schermata salva
    def menu_save(self):
           # Apre un dialog per scegliere nome e posizione del file
           file_name, _ = QFileDialog.getSaveFileName(
               self, 
               "Save File", 
               "output.txt",  # Nome file suggerito inizialmente
               "Text Files (*.txt)"  # Filtro per mostrare solo file .txt
           )
           if file_name:  # Se l'utente ha scelto un nome e premuto "Salva"
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

               with open(file_name, "w") as file:
                   for key, value in data.items():
                       file.write(f"{key}: {value}\n")

               QMessageBox.information(self, "Saved", f"Data has been saved to {file_name}")
    
    # Implementazione del caricamento
    def menu_load(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Load File", "", "Text Files (*.txt)")
        if file_name:
            widgets = self.centralWidget().layout()
            with open(file_name, "r") as file:
                lines = file.readlines()
                data = {line.split(": ")[0]: line.split(": ")[1].strip() 
                       for line in lines if ": " in line}
            
            # Riempire i campi
            widgets.itemAt(1).widget().setText(data.get("Vorname", ""))
            widgets.itemAt(3).widget().setText(data.get("Name", ""))
            dformat = QLocale().dateFormat(format=QLocale.FormatType.ShortFormat)
            widgets.itemAt(5).widget().setDate(
                QDate.fromString(data.get("Geburtstag", ""), "dd MM yyyy"))
            widgets.itemAt(7).widget().setText(data.get("Adresse", ""))
            widgets.itemAt(9).widget().setText(data.get("Postleitzahl", ""))
            widgets.itemAt(11).widget().setText(data.get("Ort", ""))
            widgets.itemAt(13).widget().setCurrentText(data.get("Land", "Schweiz"))

    def menu_quit(self):
        print("Quit")
        self.close()

## COLLEGAMENTO CON GOOGLE MAPS
    ## Funzione per aprire Google Maps
    def open_google_maps(self):
        # Raccogli i dati dai campi
        widgets = self.centralWidget().layout()
        adresse = widgets.itemAt(7).widget().text()  # Adresse
        plz = widgets.itemAt(9).widget().text()      # Postleitzahl
        ort = widgets.itemAt(11).widget().text()     # Ort
        land = widgets.itemAt(13).widget().currentText()  # Land

        maps_link = f"https://www.google.ch/maps/place/{adresse}+{plz}+{ort}+{land}"

        # Apri il link nel browser predefinito
        QDesktopServices.openUrl(QUrl(maps_link))   

    ##Permette di creare la finestra
    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("Personen Daten")
        
        ### LAYOUT WÄHLEN:
        layout = QFormLayout()
        self.setMinimumSize(1720, 880)

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
        ## Neue Button erstellt
        BottonAufKarteZeigen = QPushButton("Auf Karte zeigen")
        BottonLaden = QPushButton("Laden")
        
        BottonSave = QPushButton("Save")

        #item in ComboBox
        LandEdit.addItems(["Schweiz", "Deutschland", "Italien", "Andere"])

        ## Layout füllen
        layout.addRow("Vorname:" , VornameLineEdit)
        layout.addRow("Nachname:" , NachnameLineEdit)
        layout.addRow("Geburtstag:" , GeburtstagDateEdit)
        layout.addRow("Adresse:" , AdresseLineEdit)
        layout.addRow("Postleizhal:" , PostLeitzhalLineEdit)
        layout.addRow("Ort:" , OrtLineEdit)
        layout.addRow("Land:", LandEdit)
        layout.addRow(BottonAufKarteZeigen)
        layout.addRow(BottonLaden)       
        layout.addRow(BottonSave)

        ## Fenster anzeigen
        self.show()
    
    def createConnects(self):
 # Connessioni corrette dei pulsanti
        layout = self.centralWidget().layout()
        layout.itemAt(14).widget().clicked.connect(self.open_google_maps)  # Auf Karte zeigen
        layout.itemAt(15).widget().clicked.connect(self.menu_load)        # Laden
        layout.itemAt(16).widget().clicked.connect(self.menu_save)        # Save
   
def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()