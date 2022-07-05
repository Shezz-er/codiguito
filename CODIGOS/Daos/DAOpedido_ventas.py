from dataclasses import dataclass
from pedido_ventas import pedido_ventas
from datetime import datetime
import mysql.connector

@dataclass

class DAOpedido_ventas:

    def insertarPedido_ventas(self, pedido_ventas:pedido_ventas):
        conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = "insert into pedido_ventas values(%s,%s,%s,%s,%s)"
        cursor.execute(sql,(pedido_ventas.idpedido, pedido_ventas.idpersona, pedido_ventas.fecha, pedido_ventas.monto, pedido_ventas.iddoc))
        conexion.commit()
        conexion.close()

    def actualizarPedido_ventas(self, pedido_ventas:pedido_ventas):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = " update idpersona = %s, fecha = %s, monto = %s where idpedido = %s"
        cursor.execute(sql,(pedido_ventas.idpersona, pedido_ventas.fecha, pedido_ventas.monto, pedido_ventas.iddoc, pedido_ventas.idpedido))
        conexion.commit()
        conexion.close()

    def eliminarPedido_ventas(self, pedido_ventas:pedido_ventas):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = f" delete from pedido_ventas where idpedido = '{pedido_ventas.idpedido}'"
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def buscarPedido_ventas(self, idpedido:int):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = f"select * from pedido_ventas where idpedido = '{idpedido}'"
        cursor.execute(sql)
        fila = cursor.fetchone()
        conexion.close()
        resultado = pedido_ventas(fila[0], fila[1], fila[2], fila[3], fila[4])
        return resultado

    def listarPedido_ventas(self):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = "select * from pedido_ventas"
        cursor.execute(sql)
        filas = cursor.fetchall()
        conexion.close()
        listPedido_ventas = list()
        for registro in filas:
            pedidoventa = pedido_ventas(registro[0], registro[1], registro[2], registro[3], registro[4])
            listPedido_ventas.append(pedidoventa)
        return listPedido_ventas