from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class ShortCalc(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulyator")

        self.ekran = QLineEdit("")
        self.v_main = QVBoxLayout()

        tugmalar = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", "C", "=", "+"]
        ]

        self.v_main.addWidget(self.ekran)

        for qator in tugmalar:
            h_lay = QHBoxLayout()
            for matn in qator:
                btn = QPushButton(matn)

                btn.clicked.connect(lambda checked, b=matn: self.bos(b))
                h_lay.addWidget(btn)
            self.v_main.addLayout(h_lay)

        self.setLayout(self.v_main)

    def bos(self, belgi):
        if belgi == "C":
            self.ekran.clear()
        elif belgi == "=":
            try:
                self.ekran.setText(str(eval(self.ekran.text())))
            except:
                self.ekran.setText("Xato")
        else:
            self.ekran.setText(self.ekran.text() + belgi)

app = QApplication([])
win = ShortCalc()
win.show()
app.exec_()