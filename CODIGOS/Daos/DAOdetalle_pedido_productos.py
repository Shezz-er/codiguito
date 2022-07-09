
from clases_carrito import *
import mysql.connector
conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
cursor = conexion.cursor()
'''
@dataclass

class DAOdetalle_pedido_productos:

    def insertarDetalle_pedido_productos(self, detalle_pedido_productos:detalle_pedido_productos):
        conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = "insert into detalle_pedido_productos(cod_prod, idpedido, cantidad) values(%s,%s,%s)"
        cursor.execute(sql,(detalle_pedido_productos.cod_prod, detalle_pedido_productos.idpedido, detalle_pedido_productos.cantidad))
        conexion.commit()
        conexion.close()

    def actualizarDetalle_pedido_productos(self, detalle_pedido_productos:detalle_pedido_productos):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = " update cod_prod = %s, idpedido = %s where iddt = %s"
        cursor.execute(sql,(detalle_pedido_productos.cod_prod, detalle_pedido_productos.idpedido, detalle_pedido_productos.iddt))
        conexion.commit()
        conexion.close()

    def eliminarDetalle_pedido_productos(self, detalle_pedido_productos:detalle_pedido_productos):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = f" delete from detalle_pedido_productos where iddt = '{detalle_pedido_productos.iddt}'"
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def buscarDetalle_pedido_productos(self, iddt:int):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = f"select * from detalle_pedido_productos where iddt = '{iddt}'"
        cursor.execute(sql)
        fila = cursor.fetchone()
        conexion.close()
        resultado = detalle_pedido_productos(fila[0], fila[1], fila[2])
        return resultado

    def listarDetalle_pedido_productos(self):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = "select * from detalle_pedido_productos"
        cursor.execute(sql)
        filas = cursor.fetchall()
        conexion.close()
        listDetalle_pedido_productos = list()
        for registro in filas:
            detallepedidoproducto = detalle_pedido_productos(registro[0], registro[1], registro[2])
            listDetalle_pedido_productos.append(detallepedidoproducto)
        return listDetalle_pedido_productos
'''

def insertarDetalle(idpedido,cod_prod,cantidad):
    query=f"INSERT INTO detalle_pedido_productos(cod_prod,idpedido,cantidad) VALUES ({cod_prod},{idpedido},{cantidad});"
    cursor.execute(query)
    conexion.commit()
    query2=f"SELECT iddt FROM detalle_pedido_productos WHERE cod_prod={cod_prod} AND idpedido={idpedido} ;"
    cursor.execute(query2)
    id_detalle= cursor.fetchone()
    #item=detalle_pedido_productos(id_detalle[0],cod_prod,idpedido,cantidad)
    return id_detalle[0]

def actualizarDetalle(idpedido,cod_prod,cantidad):
    query=f"UPDATE detalle_pedido_productos SET cantidad={cantidad} WHERE idpedido={idpedido} AND cod_prod={cod_prod} ;"
    cursor.execute(query)
    conexion.commit()
    return

def mostrarDetalle(iddt):
    query=f"SELECT * FROM detalle_pedido_productos WHERE iddt={iddt} ;"
    cursor.execute(query)
    conexion.commit()
    detalle=cursor.fetchone()
    return detalle

#metodos de pedido_ventas
def obtenerDetallePedido(iddt):
    query="SELECT * FROM detalle_pedido_productos WHERE iddt=%s ;"
    cursor.execute(query,(iddt,))
    resultado=cursor.fetchone()
    return Registro_detalle(resultado[0],resultado[1],resultado[2],resultado[3])


