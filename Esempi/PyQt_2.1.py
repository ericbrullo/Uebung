import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

    def createLayout(self):
        self.setWindowTitle("Demo")
        layout = QGridLayout()

        self.button = QPushButton("Button 1")
        self.linedit = QLineEdit()
        self.checkbox = QCheckBox("Check")
        self.checkbox.setCheckState(Qt.CheckState.Checked)
        self.radio1 = QRadioButton("Radio 1")
        self.radio2 = QRadioButton("Radio 2")
        self.calender = QCalendarWidget()
        self.combobox = QComboBox()
        self.combobox.addItems(["Eins", "Zwei", "Drei"])

        layout.addWidget(self.button)
        layout.addWidget(self.linedit)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.calender)
        layout.addWidget(self.combobox)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

        self.show()

    def createConnects(self):
        self.button.clicked.connect(self.button_clicked)
        self.linedit.textChanged.connect(self.lineedit_update)
        self.checkbox.stateChanged.connect(self.check_boxchanged)
        self.radio1.toggled.connect(self.radio1_toggled)
        self.radio2.toggled.connect(self.radio2_toggled)
        self.calender.clicked.connect(self.calendar_clicked)
        self.combobox.activated.connect(self.combobox_indexchange)

    def button_clicked(self):
        print("Button clicked")

    def lineedit_update(self, txt):
        print("Text changed:", txt)

    def check_boxchanged(self, state):
        if state == Qt.CheckState.Checked:
            print("Checkbox is checked")
        elif state == Qt.CheckState.Unchecked:
            print("Checkbox is unchecked")


    def radio1_toggled(self, checked):
        print("Radio 1", checked)

    def radio2_toggled(self, checked):
        print("Radio 2", checked)

    def calendar_clicked(self, date):
        print(date)

    def combobox_indexchange(self, index):
        print(index)
    


def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()