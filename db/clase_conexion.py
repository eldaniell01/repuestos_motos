import mysql.connector

class ConexionMySQL:
    def __init__(self, host, usuario, contrasena, base_datos):
        self.host = host
        self.usuario = usuario
        self.contrasena = contrasena
        self.base_datos = base_datos
        self.conexion = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.contrasena,
                database=self.base_datos
            )
            self.cursor = self.conexion.cursor()
            print("Conexión exitosa a la base de datos MySQL")
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos MySQL:", error)

    def ejecutar_consulta(self, consulta):
        try:
            self.cursor.execute(consulta)
            resultados = self.cursor.fetchall()
            return resultados
        except mysql.connector.Error as error:
            print("Error al ejecutar la consulta:", error)

    def cerrar_conexion(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada a la base de datos MySQL")