import sys
from PyQt5.QtWidgets import QApplication, QGraphicsDropShadowEffect, QWidget, QMainWindow,  QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import Qt,QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor
from interfaz.ver_repuestos import Show_repuestos
from interfaz.registrar_repuesto import R_repuestos

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName('fondo')
        self.style_sheet = f"""
            #fondo{{
                background-color: #026E81;
                
            }}
            #boton{{
                background-color: #FF9933; 
                min-width: 300px;
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
            #cuadro{{
                background-color: #A1C7E0;
                max-width: 400px;
                
               
                
            }}
        """
        self.setWindowTitle('HOME')
        self.setFixedSize(800, 600)
        self.setStyleSheet(self.style_sheet) 
        self.initUI()
        

    def initUI(self):
        
        self.layout = QGridLayout()
        self.recibo = QPushButton('RECIBO', self)
        self.repuestos = QPushButton('VER REPUESTOS', self)
        self.rRepuesto = QPushButton('REGISTRAR PRODUCTO', self)
        
        self.layout.addWidget(self.recibo,0,0)
        self.layout.addWidget(self.repuestos,1,0)
        self.layout.addWidget(self.rRepuesto,2,0)
        self.recibo.setObjectName('boton')
        self.repuestos.setObjectName('boton')
        self.rRepuesto.setObjectName('boton')
        

        self.repuestos.clicked.connect(self.abrirVentana)
        self.rRepuesto.clicked.connect(self.reg_productos)
        self.shadow = QGraphicsDropShadowEffect()
        self.recibo.enterEvent = lambda event: self.button_enterEvent(self.recibo)
        self.recibo.leaveEvent = lambda event: self.button_leaveEvent(self.recibo)
        
        self.repuestos.enterEvent = lambda event: self.button_enterEvent(self.repuestos)
        self.repuestos.leaveEvent = lambda event: self.button_leaveEvent(self.repuestos)
        
        self.rRepuesto.enterEvent = lambda event: self.button_enterEvent(self.rRepuesto)
        self.rRepuesto.leaveEvent = lambda event: self.button_leaveEvent(self.rRepuesto)
        
        self.widget = QWidget()
        self.widget.setObjectName('cuadro')
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.layout.setAlignment(Qt.AlignCenter)

    def abrirVentana(self):
        # Crea una instancia de la otra ventana y la muestra
        self.ventana_secundaria = Show_repuestos()
        self.ventana_secundaria.show()
        
    def reg_productos(self):
        self.rproducto = R_repuestos()
        self.rproducto.show()
        
    def button_enterEvent(self, boton):
        # Crear una animación para activar el efecto de sombra suavemente
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(0, 0, 0, 180))  # Color de la sombra
        shadow.setBlurRadius(15)  # Radio del desenfoque de la sombra
        shadow.setOffset(2, 2) 
        boton.setGraphicsEffect(shadow)
      
       

    def button_leaveEvent(self, boton):
        # Crear una animación para desactivar el efecto de sombra suavemente
        boton.setGraphicsEffect(None) 
        

'''class ventana:
    
    def create_window():
        app = QApplication(sys.argv)
        ventana = Show_repuestos()   
        letra = QFont('Arial',12)
        window = QWidget()
        window.setWindowTitle('Mi Primera Ventana')
        window.setGeometry(100, 100, 800, 600)  
        window.setObjectName('fondo')
        window.setFont(letra)
        
        
        
        imagen = QLabel()
        layout = QGridLayout()
        window.setLayout(layout)
        
        img = 'img/ce7edb72-839a-4c69-9a2d-2510b67bc370.jpg'
                
                
        button1 = QPushButton('VENDER')
        button2 = QPushButton('VER RECIBOS')
                
        imagen.setObjectName('imagen-l')  
        button1.setObjectName("button")
        button2.setObjectName('button')
        
        
        layout.addWidget(button1, 0, 0)
        layout.addWidget(button2, 1, 0)
        layout.addWidget(imagen, 0,1,3,1)
       
        style_sheet = f"""
        #imagen-l {{
            background-image: url({img});
            border-radius: 15px;
            border: 1px solid;
            background-position:center;
            background-repeat:no-repeat;
            width:150px;
            height:150px;
        }}

        #button{{
            background-color: #B4BEC9; 
            min-width: 200px;
            height: 50px;
            margin: 5px 20px 5px 20px;
            color: red;
            border: 1px solid; 
            border-radius: 5px;
            font-size: 20px;
            font-family:'Droid Sans Mono', 'monospace', monospace;
            font-weight:bold;                      
        }}
        
        #button:hover{{
            background-color: #DEEFE7;
            
        }}
        
        #fondo{{
            background-color: #A6A6A6;
        }}
        """
        def ventana2(self):
            self.ventana = ventana
            self.ventana.show()
        button1.clicked.connect(ventana2)
        window.setStyleSheet(style_sheet)
        window.show()

        # Ejecutar el bucle de eventos de la aplicación
        sys.exit(app.exec_())'''
