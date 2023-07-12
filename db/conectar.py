from db.clase_conexion import ConexionMySQL

class Consultas:
    def __init__(self):
        self.conexion = ConexionMySQL()
        self.conexion.conectar()
        
    def consultar_repuesto(self):
        resultado = self.conexion.ejecutar_consulta(f"""
                                                    select repuesto.cod_repuesto as CODIGO, repuesto.name_repuesto as REPUESTO, repuesto.description as DESCRIPCION, repuesto.precio as PRECIO,  proveedor.name_pro as PROVEEDOR, moto.name_moto as MOTO  from repuesto
	                                                    inner join moto on repuesto.moto_idmoto = moto.idmoto
                                                        inner join proveedor on repuesto.proveedor_idproveedor = proveedor.idproveedor
                                                    """)
        print(resultado)
        self.conexion.cerrar_conexion()
        return resultado
        

