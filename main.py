import sys
from interfaz.principal import VentanaPrincipal
from PyQt5.QtWidgets import QApplication



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())