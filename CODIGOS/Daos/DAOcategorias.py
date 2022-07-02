from dataclasses import dataclass
from Tablas.categorias import categorias
import mysql.connector

@dataclass

class DAOcategorias:

    def insertarCategorias(self, categorias:categorias):
        conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = "insert into categorias values(%s,%s,%s)"
        cursor.execute(sql,(categorias.idcategorias, categorias.nombre_cat, categorias.descripcion_cat))
        conexion.commit()
        conexion.close()

    def actualizarCategorias(self, categorias:categorias):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = " update nombre_cat = %s, descripcion_cat = %s where idcategorias = %s"
        cursor.execute(sql,(categorias.nombre_cat, categorias.descripcion_cat, categorias.idcategorias))
        conexion.commit()
        conexion.close()

    def eliminarCategorias(self, categorias:categorias):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = f" delete from categorias where idcategorias = '{categorias.idcategorias}'"
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def buscarCategorias(self, idcategorias:int):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = f"select * from categorias where idcategorias = '{idcategorias}'"
        cursor.execute(sql)
        fila = cursor.fetchone()
        conexion.close()
        resultado = categorias(fila[0], fila[1], fila[2])
        return resultado

    def listarCategorias(self):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = "select * from categorias"
        cursor.execute(sql)
        filas = cursor.fetchall()
        conexion.close()
        listcategorias = list()
        for registro in filas:
            categorias = categorias(registro[0], registro[1], registro[2])
            listcategorias.append(categorias)
        return listcategorias