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
        
    def consultar_proveedor(self):
        proveedor = self.conexion.ejecutar_consulta(f"""
                                                    select *from proveedor
                                                    """)
        print(proveedor)
        self.conexion.cerrar_conexion()
        return proveedor
    
    def consultar_motos(self):
        motos = self.conexion.ejecutar_consulta(f"""
                                                select * from moto
                                                """)
        print(motos)
        self.conexion.cerrar_conexion()
        return motos
    
    def inset_repuesto(self, cod, name, description, precio, proveedor, moto):
        query = """
            INSERT INTO repuesto(cod_repuesto, name_repuesto, description, precio, moto_idmoto, proveedor_idproveedor)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        values = (cod, name, description, precio, int(moto), int(proveedor))
        
        self.conexion.ejecutar_consulta(query, values)
        self.conexion.cerrar_conexion()