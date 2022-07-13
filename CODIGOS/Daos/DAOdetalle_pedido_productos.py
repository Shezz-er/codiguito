
from clases_carrito import *
import mysql.connector
conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
cursor = conexion.cursor()

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


