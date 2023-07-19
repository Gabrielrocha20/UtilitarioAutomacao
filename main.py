import sys
import typing
from threading import Thread
from time import sleep

from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow

from liberar import PegarLiberacao
from ui import Ui_MainWindow


class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.thread = {}
        self.btnLiberarArara.clicked.connect(self.liberarArara)

        self.PageLiberarArara.clicked.connect(lambda: self.Windown.setCurrentWidget(self.Arara))

    def liberarArara(self):
        cnpj = self.inputCNPJ.text()
        self.btnLiberarArara.setEnabled(False)

        self.thread[1] = QTTread(parent=None, index=1, cnpj=cnpj)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.setlabel)
        
        

    def setlabel(self, liberacao):

        arara, pdv = liberacao.split('//')

        
        self.labelLiberarArara.setText(arara)
        self.labelLiberarPdv.setText(pdv)
        self.btnLiberarArara.setEnabled(True)

class QTTread(QThread):
    any_signal = pyqtSignal(str)
    def __init__(self, parent=None, index=0, cnpj=None):
        super(QTTread, self).__init__(parent)
        self.index = index
        self.is_running = True
        self.cnpj = cnpj

    def run(self):
        PegarArara = PegarLiberacao()
        liberacao = PegarArara.liberar(self.cnpj)
        self.any_signal.emit(liberacao)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loja = Interface()
    loja.show()
    app.exec()


"""
    DataHex ERP | Arara
    Chave de acesso: 70119736001021

    Validade da chave: 18/07/2023

    PDV
    Chave de acesso: 70219736001020

    Validade da chave: 18/07/2023
"""