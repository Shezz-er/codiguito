
import mysql.connector
from clases_carrito import *

conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
cursor = conexion.cursor()
'''
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
