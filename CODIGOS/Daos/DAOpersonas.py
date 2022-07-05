from dataclasses import dataclass
from personas import personas
import mysql.connector

@dataclass

class DAOpersonas:

    def insertarPersonas(self, personas:personas):
        conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = "insert into personas values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(personas.idpersona, personas.rut, personas.nombre_persona, personas.apellido, personas.telefono, personas.direccion, personas.email_user, personas.password, personas.idrol))
        conexion.commit()
        conexion.close()

    def actualizarPersonas(self, personas:personas):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = " update rut = %s, nombre_persona = %s, apellido = %s telefono = %s, direccion = %s, email_user = %s password = %s, idrol = %s where idpersona = %s"
        cursor.execute(sql,(personas.rut, personas.nombre_persona, personas.apellido, personas.telefono, personas.direccion, personas.email_user, personas.password, personas.idrol, personas.idpersona))
        conexion.commit()
        conexion.close()
    
    def eliminarPersonas(self, personas:personas):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = f" delete from personas where idpersona = '{personas.idpersona}'"
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def buscarPersonas(self, idpersona:int):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = f"select * from personas where idpersona = '{idpersona}'"
        cursor.execute(sql)
        fila = cursor.fetchone()
        conexion.close()
        resultado = personas(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8])
        return resultado

    def listarPersonas(self):
        conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        sql = "select * from personas"
        cursor.execute(sql)
        filas = cursor.fetchall()
        conexion.close()
        listPersonas = list()
        for registro in filas:
            persona = personas(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], registro[8])
            listPersonas.append(persona)
        return listPersonas