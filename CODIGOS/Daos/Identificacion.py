from dataclasses import dataclass
from MenuFuncionarios import MenuFuncionarios
from clases_carrito import *
from login import *
dao=MenuFuncionarios

@dataclass

class Identificacion:

    def menuIdentificacion():
        print ("I D E N T I F I Q U E S E")
        print ("--------------------------")
        idpersona=int(input("Ingrese su Id de Usuario: "))
        password=input("Ingrese su Contraseña: ")

        login = Login(idpersona,password)
        if exists(login):
            print("Acceso Correcto")
            user=DAOpersonas.getUser(login.id)

            if user.idrol==2:
                dao.ejecutarMenuJefeventa(user)
            else:
                dao.ejecutarMenuVendedor(Vendedor(user.idpersona,user.rut,user.nombre_persona,user.apellido,user.telefono,user.direccion,user.email_user,user.password))
        else:
            print("ID y/o contraseña no corresponden")
            return Identificacion.menuIdentificacion()

