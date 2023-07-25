import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QGridLayout, QGraphicsDropShadowEffect, QLabel, QMainWindow, QFrame, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from db.conectar import Consultas
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
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
                margin-top: 30px;
                
                
                max-height: 300px;
            }}
            #cuadro2{{
                background-color: #A1C7E0;
                border-radius:5px;
                max-height: 200px;
            }}
            #filtro{{
                border-radius: 6px;
                color: red;
                height: 40px;
                font-size: 16px;
                font-family: 'MesloLGS_NF_Bold', 'monospace', monospace;
                font-weight:bold;
            }}
            #boton{{
                background-color: #FF9933;
                min-width: 400px; 
                height: 50px;
                margin: 10px;
                color: red;
                border-radius: 6px;
                font-size: 16px;
                font-family: 'MesloLGS_NF_Bold', 'monospace', monospace;
                font-weight:bold;                      
            }}
            #boton:hover{{
                background-color: #FF9933;
                border: none; 
            }}
            
            #texto{{
                
                color: red;
                font-size: 18px;
                font-family: 'MesloLGS_NF_Bold', 'monospace', monospace;
                font-weight:bold;
            }}
            #tabla{{
                font-size: 14px;
                font-family: 'MesloLGS_NF_Bold', 'monospace', monospace;
                font-weight:bold;
            }}
        """
        self.setWindowTitle('VER PRODUCTOS')
        self.setFixedSize(800, 600)
        self.setStyleSheet(self.styles)  
        self.initUI()
        

    def initUI(self):
        # Crear un botón para abrir la otra ventana
        # Widget principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Diseño principal
        self.main_layout = QGridLayout(central_widget)

        # Cuadro de texto y botón
        self.rotulo = QLabel('BUSQUEDA DE PRODUCTOS', self)
        self.rotulo.setObjectName('texto')
        self.textbox = QLineEdit(self)
        self.textbox.setObjectName('filtro')
        self.upd = QPushButton('ACTUALIZAR LISTA DE PRODUCTOS', self)
        self.upd.setObjectName('boton')

        # Tabla
        self.table_widget = QTableWidget(self)
        self.table_widget.setObjectName('tabla')

        # Frame del cuadro de texto y el botón
        form_frame = QFrame()
        form_frame.setObjectName('cuadro2')
        form_layout = QGridLayout(form_frame)
        form_layout.addWidget(self.rotulo,0, 0, 1, 1, alignment=Qt.AlignCenter)
        form_layout.addWidget(self.textbox,1,0)
        form_layout.addWidget(self.upd,2,0,1, 1, alignment=Qt.AlignCenter)
        form_layout.setAlignment(Qt.AlignCenter)
        # Agregar frame del cuadro de texto y el botón al diseño principal
        self.upd.enterEvent = lambda event: self.shadow_active(self.upd)
        self.upd.leaveEvent = lambda event: self.shadow_deactive(self.upd)
        self.main_layout.addWidget(form_frame)
    

        # Frame de la tabla
        self.frame = QFrame(self)
        self.frame.setObjectName('cuadro1')
        self.show_repuestos()

        # Conexión de señales y slots
        self.textbox.textChanged.connect(self.filter_producto)
           
    def show_repuestos(self):
        sombra = QGraphicsDropShadowEffect()
        sombra.setColor(QColor(0, 0, 0, 180))
        sombra.setBlurRadius(20)
        sombra.setOffset(0,0)
        columnas =['CODIGO', 'REPUESTO', 'DESCRIPCION', 'PRECIO', 'PROVEEDOR', 'MOTO']
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
        self.main_layout.addWidget(self.frame,1,0)
    
    def filter_producto(self):
        filtrar = self.textbox.text().upper()
        for row in range(self.table_widget.rowCount()):
            row_text=[self.table_widget.item(row, col).text().upper() for col in range(self.table_widget.columnCount())]
            print(row_text)
            if any(filtrar in text for text in row_text):
                self.table_widget.setRowHidden(row, False)
            else:
                self.table_widget.setRowHidden(row,True)
           
    def shadow_active(self, objeto):
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(0,0,0,180))
        shadow.setBlurRadius(15)
        shadow.setOffset(2,2)
        objeto.setGraphicsEffect(shadow)   
    
    def shadow_deactive(self, objeto):
        objeto.setGraphicsEffect(None)
    
   