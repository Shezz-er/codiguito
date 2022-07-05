from dataclasses import dataclass
from estado_jornada import estado_jornada
import mysql.connector

@dataclass

class DAOestado_jornada:

    def insertarEstado_jornada(self, estado_jornada:estado_jornada):
        conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = "insert into estado_jornada values(%s,%s)"
        cursor.execute(sql,(estado_jornada.cod_estado, estado_jornada.estado))
        conexion.commit()
        conexion.close()

    def actualizarEstado_jornada(self, estado_jornada:estado_jornada):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = " update estado = %s where cod_estado = %s"
        cursor.execute(sql,(estado_jornada.estado, estado_jornada.cod_estado))
        conexion.commit()
        conexion.close()

    def eliminarEstado_jornada(self, estado_jornada:estado_jornada):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = f" delete from estado_jornada where cod_estado = '{estado_jornada.cod_estado}'"
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def buscarEstado_jornada(self, cod_estado:int):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = f"select * from estado_jornada where cod_estado = '{cod_estado}'"
        cursor.execute(sql)
        fila = cursor.fetchone()
        conexion.close()
        resultado = estado_jornada(fila[0], fila[1])
        return resultado

    def listarEstado_jornada(self):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = "select * from estado_jornada"
        cursor.execute(sql)
        filas = cursor.fetchall()
        conexion.close()
        listEstado_jornada = list()
        for registro in filas:
            estadojornada = estado_jornada(registro[0], registro[1])
            listEstado_jornada.append(estadojornada)
        return listEstado_jornada