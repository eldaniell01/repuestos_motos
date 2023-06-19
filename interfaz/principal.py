import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Crear una aplicación de PyQt
app = QApplication(sys.argv)

# Crear una ventana
window = QWidget()
window.setWindowTitle('Mi Primera Ventana')
window.setGeometry(100, 100, 300, 200)  # Establecer posición y tamaño de la ventana

# Mostrar la ventana
window.show()

# Ejecutar el bucle de eventos de la aplicación
sys.exit(app.exec_())
