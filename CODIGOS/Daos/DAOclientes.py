
from clases_carrito import *
import mysql.connector

conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
cursor = conexion.cursor()

def verificarCliente(rut):
    query="SELECT COUNT(*) FROM clientes WHERE rut_cliente=%s ;"
    cursor.execute(query,(rut,))
    resultado=cursor.fetchone()
    return resultado[0]

def insertarCliente(rut,razon,giro,direccion):
    query="INSERT INTO clientes VALUES (%s,%s,%s,%s);"
    cursor.execute(query,(rut,razon,giro,direccion))
    conexion.commit()
    return Cliente(rut,razon,giro,direccion)

def obtenerCliente(rut):
    query="SELECT * FROM clientes WHERE rut_cliente=%s ;"
    cursor.execute(query,(rut,))
    resultado=cursor.fetchone()
    return Cliente(resultado[0],resultado[1],resultado[2],resultado[3])

