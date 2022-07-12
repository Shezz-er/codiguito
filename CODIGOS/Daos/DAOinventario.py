
import mysql.connector
from clases_carrito import *

conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
cursor = conexion.cursor()
'''
@dataclass

class DAOinventario:

    def insertarInventario(self, inventario:inventario):
        conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = "insert into inventario values(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(inventario.idinventario, inventario.cod_prod, inventario.nom_prod, inventario.stock_prod, inventario.precio_prod, inventario.descripcion_prod, inventario.idcategorias))
        conexion.commit()
        conexion.close()

    def actualizarInventario(self, inventario:inventario):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = " update cod_prod = %s, nom_prod = %s, stock_prod = %s precio_prod = %s, descripcion_prod = %s, idtipiproducto = %s where idinventario = %s"
        cursor.execute(sql,(inventario.cod_prod, inventario.nom_prod, inventario.stock_prod, inventario.precio_prod, inventario.descripcion_prod, inventario.idcategorias, inventario.idinventario))
        conexion.commit()
        conexion.close()

    def eliminarInventario(self, inventario:inventario):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = f" delete from inventario where idinventario = '{inventario.idinventario}'"
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def buscarInventario(self, idinventario:int):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = f"select * from inventario where idinventario = '{idinventario}'"
        cursor.execute(sql)
        fila = cursor.fetchone()
        conexion.close()
        resultado = inventario(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
        return resultado

    def listarInventario(self):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = "select cod_prod, nom_prod from inventario"
        cursor.execute(sql)
        filas = cursor.fetchall()
        conexion.close()
        listInventario = list()
        for registro in filas:
            producto = inventario(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
            listInventario.append(producto)
        return listInventario



atributo="123"
conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
cursor = conexion.cursor()
query="SELECT cod_prod, nom_prod, precio_prod FROM inventario WHERE cod_prod=CAST(%s AS UNSIGNED INT) OR nom_prod=%s ;"
cursor.execute(query,(atributo,atributo))
resultado=cursor.fetchone()

print(resultado)
'''

def obtenerProducto(atributo):
    query="SELECT cod_prod, nom_prod, precio_prod FROM inventario WHERE cod_prod=CAST(%s AS UNSIGNED INT) OR nom_prod=%s ;"
    cursor.execute(query,(atributo,atributo))
    resultado=cursor.fetchone()
    return Producto(resultado[0],resultado[1],resultado[2])

def listarProductos():
    query="SELECT * FROM inventario ;"
    cursor.execute(query)
    lista=cursor.fetchall()
    return lista