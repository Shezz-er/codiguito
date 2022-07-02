from dataclasses import dataclass
from Tablas.detalle_pedido_productos import detalle_pedido_productos
import mysql.connector

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