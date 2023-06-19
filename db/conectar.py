from clase_conexion import ConexionMySQL

conn = ConexionMySQL(base_datos='repuesto_motos',contrasena='12Intercambios',host='localhost', usuario='root')
conn.conectar()
resultados = conn.ejecutar_consulta("SELECT * FROM repuesto")
for resultado in resultados:
    print(resultado)
    
conn.cerrar_conexion()