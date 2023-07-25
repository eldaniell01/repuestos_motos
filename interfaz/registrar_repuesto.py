import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QComboBox, QHBoxLayout, QGridLayout, QGraphicsDropShadowEffect, QLabel, QMainWindow, QFrame, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from db.conectar import Consultas
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class R_repuestos(QMainWindow):
    def __init__(self, ):
        super().__init__()
        self.setObjectName('fondo')
        self.styles = f"""
            #fondo{{
                background-color: #026E81;
            }}
            
            #formulario{{
                background-color: #A1C7E0;
                border-radius:5px;
                max-width: 700px;
                
            }}
            
            #rotulo{{
                margin: 10px;
                color: red;
                font-size: 20px;
                font-family: 'MesloLGS_NF_Bold', 'monospace', monospace;
                font-weight:bold;
            }}
            
            #labes{{
                font-size: 16px;
                font-family: 'MesloLGS_NF_Bold', 'monospace', monospace;
                font-weight:bold;
                color: red;
            }}
            
            #text{{
                max-width: 500px;
                margin: 6px;
                border-radius: 6px;
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
        """
        self.setWindowTitle('REGISTRO DE PRODUCTOS')
        self.setFixedSize(800, 600)
        self.setStyleSheet(self.styles)
        self.initUI()
    
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QGridLayout(central_widget)
        
        # objetos
        self.rotulo = QLabel('REGISTRO DE PRODUCTOS', self)
        self.rotulo.setObjectName('rotulo')
        self.labelcod= QLabel('CÓDIGO', self)
        self.labelcod.setObjectName('labes')
        self.textcod = QLineEdit(self)
        self.textcod.setObjectName('text')
        self.labelname = QLabel('PRODUCTO', self)
        self.labelname.setObjectName('labes')
        self.textname = QLineEdit(self)
        self.textname.setObjectName('text')
        self.labeldes = QLabel('DESCRIPCIÓN', self)
        self.labeldes.setObjectName('labes')
        self.textdes = QLineEdit(self)
        self.textdes.setObjectName('text')
        self.labelpre = QLabel('PRECIO', self)
        self.labelpre.setObjectName('labes')
        self.textpre = QLineEdit(self)
        self.textpre.setObjectName('text')
        self.labelpro = QLabel('PROVEEDOR', self)
        self.labelpro.setObjectName('labes')
        self.textpro = QComboBox(self)
        self.textpro.setObjectName('text')
        self.labelmoto = QLabel('MOTO', self)
        self.labelmoto.setObjectName('labes')
        self.textmoto = QComboBox(self)
        self.textmoto.setObjectName('text')
        self.reg = QPushButton('REGISTRAR PRODUCTO', self)
        self.reg.setObjectName('boton')
        
        #formulario
        self.form_frame = QFrame()
        self.form_frame.setObjectName('formulario')
        self.form_layout = QGridLayout(self.form_frame)
        self.form_layout.addWidget(self.rotulo, 0, 0, 1, 2, alignment=Qt.AlignCenter)
        self.form_layout.addWidget(self.labelcod,1,0)
        self.form_layout.addWidget(self.textcod, 1,1)
        self.form_layout.addWidget(self.labelname,2,0)
        self.form_layout.addWidget(self.textname, 2,1)
        self.form_layout.addWidget(self.labeldes, 3,0)
        self.form_layout.addWidget(self.textdes, 3,1)
        self.form_layout.addWidget(self.labelpre, 4,0)
        self.form_layout.addWidget(self.textpre, 4,1)
        self.form_layout.addWidget(self.labelpro, 5,0)
        self.form_layout.addWidget(self.textpro, 5,1)
        self.form_layout.addWidget(self.labelmoto, 6,0)
        self.form_layout.addWidget(self.textmoto, 6,1)
        self.form_layout.addWidget(self.reg, 7,0, 1,2,alignment=Qt.AlignCenter)
        self.form_layout.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.form_frame)
        
        #carga de datos o procesos
        self.reg.clicked.connect(self.registrar)
        self.reg.enterEvent = lambda event: self.shadow_active(self.reg)
        self.reg.leaveEvent = lambda event: self.shadow_deactive(self.reg)
        self.show_proveedores()
        self.show_motos()
        
    def show_proveedores(self):
        proveedor = Consultas()
        diccionario = proveedor.consultar_proveedor()
        opciones = [str(opcion[1]) for opcion in diccionario]
        self.textpro.addItems(opciones)
        print(diccionario)  
        
    def show_motos(self):
        moto = Consultas()
        diccionario = moto.consultar_motos()
        opciones = [str(opcion[1]) for opcion in diccionario]
        self.textmoto.addItems(opciones)
        print(diccionario)
        
    def shadow_active(self, objeto):
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(0,0,0,180))
        shadow.setBlurRadius(15)
        shadow.setOffset(2,2)
        objeto.setGraphicsEffect(shadow)   
    
    def shadow_deactive(self, objeto):
        objeto.setGraphicsEffect(None)
        
    def registrar(self):
        db = Consultas()
        pp = Consultas()
        motos = db.consultar_motos()
        proveedores= pp.consultar_proveedor()
        cod = self.textcod.text().upper()
        name = self.textname.text().upper()
        description = self.textdes.text().upper()
        precio = float(self.textpre.text())
        pro= self.textpro.currentText()
        moto = self.textmoto.currentText()
        
        
        idmoto = next((item[0] for item in motos if item[1]==moto), None)
        idpro = next((item[0] for item in proveedores if item[1]==pro), None)
        registro = Consultas()
        registro.inset_repuesto(cod=cod, name=name, description=description, precio=precio, proveedor=idpro, moto=idmoto)
        