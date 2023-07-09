from db.clase_conexion import ConexionMySQL

class Consultas:
    def __init__(self):
        self.conexion = ConexionMySQL()
        self.conexion.conectar()
        
    def consultar_repuesto(self):
        resultado = self.conexion.ejecutar_consulta("SELECT * FROM repuesto")
        print(resultado)
        self.conexion.cerrar_conexion()
        return resultado
        

