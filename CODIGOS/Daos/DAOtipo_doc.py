from dataclasses import dataclass
from Tablas.tipo_doc import tipo_doc
import mysql.connector

@dataclass

class DAOtipo_doc:

    def insertarTipo_doc(self, tipo_doc:tipo_doc):
        conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = "insert into tipo_doc values(%s,%s)"
        cursor.execute(sql,(tipo_doc.iddoc, tipo_doc.nombre_doc))
        conexion.commit()
        conexion.close()

    def actualizarTipo_doc(self, tipo_doc:tipo_doc):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = " update nombre_doc = %s where iddoc = %s"
        cursor.execute(sql,(tipo_doc.nombre_doc, tipo_doc.iddoc))
        conexion.commit()
        conexion.close()

    def eliminarTipo_doc(self, tipo_doc:tipo_doc):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = f" delete from tipo_doc where iddoc = '{tipo_doc.iddoc}'"
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def buscarTipo_doc(self, iddoc:int):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = f"select * from tipo_doc where iddoc = '{iddoc}'"
        cursor.execute(sql)
        fila = cursor.fetchone()
        conexion.close()
        resultado = tipo_doc(fila[0], fila[1])
        return resultado

    def listarTipo_doc(self):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = "select * from tipo_doc"
        cursor.execute(sql)
        filas = cursor.fetchall()
        conexion.close()
        listTipo_doc = list()
        for registro in filas:
            tipodoc = tipo_doc(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], registro[8])
            listTipo_doc.append(tipodoc)
        return listTipo_doc