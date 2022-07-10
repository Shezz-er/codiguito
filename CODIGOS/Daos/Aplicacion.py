from dataclasses import dataclass

from Identificacion import Identificacion

dao=Identificacion

@dataclass

class Aplicacion:

    def ejecutarAplicacion():
        print ("B I E N V E N I D O")
        print ("--------------------------")
        print ("¿Desea iniciar el programa?")
        print ("1. Si")
        print ("2. No")
        print ("3. Salir del menú")
        print ("\nSeleccione una opción:\n")
        opcion3=int(input())
    
        if opcion3==1:
            dao.menuIdentificacion()
        elif opcion3==2:
            print("Ok, vuelva cuando quiera.")
        elif opcion3==3:
            return False
        else:
            input("Error, debe ingresar una opción válida.\n")
            return False
            
    ejecutarAplicacion()