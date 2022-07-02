from dataclasses import dataclass
from DAOpedido_ventas import DAOpedido_ventas
from DAOinventario import DAOinventario
from DAOpersonas import DAOpersonas
from DAOdetalle_pedido_productos import DAOdetalle_pedido_productos

dao1=DAOpersonas
dao2=DAOpedido_ventas
dao3=DAOinventario
dao4=DAOdetalle_pedido_productos

@dataclass

class DAOMenuEjecutable:

    def ejecutarMenuJefeventa():
        print ("Bienvenido, Jefe de venta")
        print ("M E N Ú")
        print ("--------------------------")
        print ("1. Buscar Venta")
        print ("2. Informe de Ventas")
        print ("3. Insertar Producto al inventario")
        print ("4. Eliminar Producto del inventario")
        print ("5. Modificar Producto del inventario")
        print ("6. Insertar nuevo Vendedor")
        print ("7. Eliminar Vendedor")
        print ("8. Modificar datos de Vendedor")
        print ("9. Listar Vendedores")
        print ("\nSeleccione una opción:\n")
        opcion=int(input())

        if opcion==1:
            dao2.buscarPedido_ventas
        
        elif opcion==2:
            dao2.listarPedido_ventas
        
        elif opcion==3:
            dao3.insertarInventario
        
        elif opcion==4:
            dao3.eliminarInventario

        elif opcion==5:
            dao3.actualizarInventario

        elif opcion==6:
            dao1.insertarPersonas

        elif opcion==7:
            dao1.eliminarPersonas
        
        elif opcion==8:
            dao1.actualizarPersonas
        
        elif opcion==9:
            dao1.listarPersonas
        
        else:
            input("Error, debe ingresar una opción válida.")

    def ejecutarMenuVendedor():
        print ("Bienvenido, Vendedor")
        print ("M E N Ú")
        print ("--------------------------")
        print ("1. Agregar Venta")
        #listar todos los productos
        #que producto desea agregar?
        #apretar el "codigo del producto"
        #cuantos?

        print ("2. Modificar Venta")
        print ("3. Eliminar Venta")
        print ("4. Buscar Venta")
        print ("5. Buscar Producto")
        print ("6. Listar Productos")
        print ("\nSeleccione una opción:\n")
        opcion=int(input())        

        while opcion==1:
            dao3.listarInventario
            producto=int(input("¿Qué producto desea agregar?"))
            cantidad=int(input("¿Cuánto deseas agregar?"))
            
            seguir=input("¿Deseas agregar otro producto?")
            if seguir==si:
                return 

            elif seguir==no #generar boleta

            else 
        
