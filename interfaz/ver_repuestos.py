import sys
from PyQt5.QtWidgets import QApplication, QGraphicsDropShadowEffect, QLabel, QMainWindow, QFrame, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from db.conectar import Consultas
from PyQt5.QtGui import QColor
class Show_repuestos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName('fondo')
        self.styles = f"""
            #fondo{{
                background-color: #026E81;
            }}
            #cuadro1{{
                background-color: #A1C7E0;
                border-radius:5px;
                margin-top: 200px;
                margin-left: 150px;
                max-width: 500px;
                max-height: 300px;
            }}
        """
        self.setWindowTitle('segunda ventana')
        self.setFixedSize(800, 600)
        self.setStyleSheet(self.styles)  
        self.initUI()
        

    def initUI(self):
        # Crear un botón para abrir la otra ventana
        self.textbox = QLineEdit(self)
        self.mostrar = QLabel('0',self)
        self.table_widget = QTableWidget(self)
        self.table_widget.setObjectName('tabla')
        self.mostrar.setGeometry(300, 200,150,200)
        self.textbox.setGeometry(210, 50, 200, 50)
        self.btn_cerrar = QPushButton('Cerrar', self)
        self.btn_cerrar.setGeometry(545, 50, 150, 30)
        self.frame = QFrame(self)
        self.frame.setObjectName('cuadro1')
        self.show_repuestos()
        self.textbox.textChanged.connect(self.filter_producto)
           
    def show_repuestos(self):
        sombra = QGraphicsDropShadowEffect()
        sombra.setColor(QColor(0, 0, 0, 180))
        sombra.setBlurRadius(20)
        sombra.setOffset(0,0)
        columnas =['NO.', 'CODIGO', 'REPUESTO', 'DESCRIPCION', 'PRECIO', 'PROVEEDOR', 'MOTO']
        mostra = Consultas()
        diccionario = mostra.consultar_repuesto()
        num_registros = len(diccionario)
        num_columnas = len(diccionario[0])
        self.table_widget.setRowCount(num_registros)
        self.table_widget.setColumnCount(num_columnas)
       
        for fila, datos in enumerate(diccionario):
            for columna, dato in enumerate(datos):
                self.table_widget.setItem(fila, columna, QTableWidgetItem(str(dato)))
        
        for columna, nombre in enumerate(columnas):
            self.table_widget.setHorizontalHeaderItem(columna, QTableWidgetItem(nombre))
        
        self.table_widget.resizeColumnsToContents()
        self.frame.setGraphicsEffect(sombra)
        layout = QVBoxLayout(self.frame)
        layout.addWidget(self.table_widget)
        self.setCentralWidget(self.frame)
    
    def filter_producto(self):
        filtrar = self.textbox.text().upper()
        for row in range(self.table_widget.rowCount()):
            row_text=[self.table_widget.item(row, col).text().upper() for col in range(self.table_widget.columnCount())]
            if any(filtrar in text for text in row_text):
                self.table_widget.setRowHidden(row, False)
            else:
                self.table_widget.setRowHidden(row,True)
           
        