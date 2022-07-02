from dataclasses import dataclass
import mysql.connector
from DAOpedido_ventas import DAOpedido_ventas
from DAOinventario import DAOinventario
from DAOpersonas import DAOpersonas
from DAOMenuEjecutable import DAOMenuEjecutable

dao1=DAOpersonas
dao2=DAOpedido_ventas
dao3=DAOinventario
dao4=DAOMenuEjecutable

@dataclass

class DAOMenu:

    def menuIde():
        conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
        cursor = conexion.cursor()
        print ("I D E N T I F I Q U E S E")
        print ("--------------------------")
        print ("1. Jefe de ventas")
        print ("2. Vendedor")
        print ("3. Salir del menú")
        print ("\nSeleccione una opción:\n")
        opcion2=int(input())

        if opcion2==1:
            usuarioNom = input("Ingrese su Nombre: ")
            usuarioApe = input("Ingrese su Apellido: ")
            contra = input("Ingrese su Contraseña")
            idrol = 2

            sql = f"select * from personas where nombre_persona = '{usuarioNom}' and apellido = '{usuarioApe}' and password = '{contra}' and idrol = '{idrol}'"
            cursor.execute(sql)
            resultado = cursor.fetchone()
            if(len(resultado)==1):
                dao4.ejecutarMenuJefeventa()
            else:
                print ("Error, Nombre, Apellido o Contraseña inválida o NO existe.")

        elif opcion2==2:
            usuarioNom = input("Ingrese su Nombre: ")
            usuarioApe = input("Ingrese su Apellido: ")
            contra = input("Ingrese su Contraseña")
            idrol = 1

            sql = f"select * from personas where nombre_persona = '{usuarioNom}' and apellido = '{usuarioApe}' and password = '{contra}' and idrol = '{idrol}'"
            cursor.execute(sql)
            resultado = cursor.fetchone()
            if(len(resultado)==1):
                print ("\nBienvenido al Sistema "), usuarioNom
                ejecutarMenuVendedor()
            else:
                print ("Error, Nombre, Apellido o Contraseña inválida o NO existe.")
                
        elif opcion2==3:
            return False
        
        else:
            input("Error, debe ingresar una opción válida.")

    def siIniciar():
        while True:
            menuIde()
    
    def menuInicio():
        print ("B I E N V E N I D O")
        print ("--------------------------")
        print ("¿Desea iniciar el programa?")
        print ("1. Si")
        print ("2. No")
        print ("3. Salir del menú")
        print ("\nSeleccione una opción:\n")
        opcion3=int(input())
    
        if opcion3==1:
            siIniciar()
        elif opcion3==2:
            print("Ok, vuelva cuando quiera.")
        elif opcion3==3:
            return False
        else:
            input("Error, debe ingresar una opción válida.")

    def ejecutar():
        while True:
            menuInicio()

    ejecutar()