from dataclasses import dataclass
from DAOpersonas import DAOpersonas
from carrito import *
import mysql.connector
import datetime

dao1=DAOpersonas


@dataclass

class MenuFuncionarios:

    def ejecutarMenuJefeventa(usuario):
        print (f"\nBienvenido, {usuario.nombre_persona}\n")
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
        print ("10. Iniciar jornada diaria")
        print ("\nSeleccione una opción:\n")
        opcion=int(input())

        if opcion==1:
            print("1.Buscar ventas mediante fecha")
            print("2.Buscar ventas mediante vendedor")
            print("Para volver al menú precione cualquier otro NÚMERO")
            print("\nSeleccione una opcion:\n")
            opcion2=int(input())

            if opcion2==1:
                conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
                cursor = conexion.cursor()
                print("Ingrese la fecha de los pedidos que desea ver en formato AAAA-MM-DD: ")
                fecha = input()
                sql = f"select count(*) from pedido_ventas where fecha = '{fecha}'"
                cursor.execute(sql)
                ventas = cursor.fetchone()
                if (ventas[0])==0:
                    print("No se encuentran ventas en la fecha especificada.")
                
                else:
                    sql = f"select * from pedido_ventas where fecha = '{fecha}'"
                    cursor.execute(sql)
                    ventas = cursor.fetchone()
                    print("\nResultados de la búsqueda: \n")
                    print("ID pedido | Id vendedor | Fecha | Monto | Id tipo documento | Rut cliente")
                    print(ventas)
                    print("\nSi desea ver el nombre y apellido del vendedor, ingrese 1. Si no, precione cualquier otro NÚMERO \n")
                    opcion3=int(input())

                    if opcion3==1:
                        print("Ingrese el Id del vendedor")
                        idpersona = input()
                        sql1 = f"select nombre_persona, apellido from personas where idpersona = '{idpersona}'"
                        cursor.execute(sql1)
                        nombreapellido = cursor.fetchone()
                        print("\nNombre:")
                        print(nombreapellido[0])
                        print("Apellido:")
                        print(nombreapellido[1])
                        conexion.close()
                        return MenuFuncionarios.ejecutarMenuJefeventa()
        
                    else:
                        return MenuFuncionarios.ejecutarMenuJefeventa()
        
            elif opcion2==2:
                conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
                cursor = conexion.cursor()
                print("Ingrese el nombre y el apellido del vendedor:")
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                sql = f"select pedido_ventas.idpedido, pedido_ventas.idpersona, pedido_ventas.fecha, pedido_ventas.monto, pedido_ventas.iddoc, pedido_ventas.rut_cliente, personas.nombre_persona, personas.apellido from pedido_ventas INNER JOIN personas on pedido_ventas.idpersona = personas.idpersona where nombre_persona = '{nombre}' and apellido = '{apellido}'"
                cursor.execute(sql)
                ventas = cursor.fetchall()
                print("\nResultados de la busqueda:\n")
                print("ID pedido | Id vendedor | Fecha | Monto | Id tipo documento | Rut cliente | Nombre Vendedor | Apellido Vendedor | ")
                #print(ventas)
                for venta in ventas:
                    print(venta)
                return MenuFuncionarios.ejecutarMenuJefeventa()

            else:
                return MenuFuncionarios.ejecutarMenuJefeventa()

        elif opcion==2:
            print("1.Listar Ventas con Boleta")
            print("2.Listar Ventas con Factura")
            print("Para volver al menú precione cualquier otro NÚMERO")
            print("\nSeleccione una opcion:\n")
            opcion=int(input())
            conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
            cursor = conexion.cursor()
            if opcion==1:
                sql = "select * from pedido_ventas where iddoc = 1"
                cursor.execute(sql)
                filas = cursor.fetchall()
                conexion.close()
                print("ID pedido | Id vendedor | Fecha | Monto | Id tipo documento | Rut cliente")
                print(filas)                    
                return MenuFuncionarios.ejecutarMenuJefeventa()

            elif opcion==2:
                sql = "select * from pedido_ventas where iddoc = 2"
                cursor.execute(sql)
                filas = cursor.fetchall()
                conexion.close()
                print("ID pedido | Id vendedor | Fecha | Monto | Id tipo documento | Rut cliente")
                print(filas)
                return MenuFuncionarios.ejecutarMenuJefeventa()
            
            else:
                return MenuFuncionarios.ejecutarMenuJefeventa()

        elif opcion==3:
            conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
            cursor = conexion.cursor()
            print("Inserte los datos del nuevo producto: ")
            nomprod = input("Nombre del producto: ")
            stockprod = int(input("Stock disponible del producto: "))
            precioprod = int(input("Precio del producto: "))
            idcategoria = int(input("Id Categoría del producto: "))
            sql = f"INSERT INTO `inventario`(`nom_prod`, `stock_prod`, `precio_prod`, `idcategorias`) VALUES ('{nomprod}','{stockprod}','{precioprod}','{idcategoria}')"
            cursor.execute(sql)
            conexion.commit()
            sql2 = f"select cod_prod, nom_prod, stock_prod, precio_prod, idcategorias from inventario where nom_prod = '{nomprod}'"
            cursor.execute(sql2)
            resultado = cursor.fetchall()
            conexion.commit()
            conexion.close()
            print("\nCodigo producto | Nombre producto | Stock disponible | Precio producto | Id categoría")
            print(resultado)
            MenuFuncionarios.ejecutarMenuJefeventa()
    
        elif opcion==4:
            print("1. Eliminar mediante Nombre de producto.")
            print("2. Eliminar mediante Codigo de producto.")
            print("Seleccione una opción\n")
            opcion=int(input())

            if opcion==1:
                conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
                cursor = conexion.cursor()
                sql0 = f"select * from inventario"
                cursor.execute(sql0)
                inv_antes = cursor.fetchall()
                nombre = input("Ingrese el nombre del producto que desea eliminar: ")
                sql = f" delete from inventario where nom_prod = '{nombre}'"
                cursor.execute(sql)
                sql1 = f"select * from inventario"
                cursor.execute(sql1)
                inv_desp = cursor.fetchall()
                if inv_antes==inv_desp:
                    print("No se ha encontrado el producto a eliminar.")
                    conexion.close()
                    return MenuFuncionarios.ejecutarMenuJefeventa()
                
                else:
                    conexion.commit()
                    print("Producto eliminado correctamente.")
                    conexion.close()
                    return MenuFuncionarios.ejecutarMenuJefeventa()
            
            elif opcion==2:
                conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
                cursor = conexion.cursor()
                sql0 = f"select * from inventario"
                cursor.execute(sql0)
                inv_antes = cursor.fetchall()
                codigo = input("Ingrese el Codigo del producto que desea eliminar: ")
                sql = f" delete from inventario where cod_prod = '{codigo}'"
                cursor.execute(sql)
                sql1 = f"select * from inventario"
                cursor.execute(sql1)
                inv_desp = cursor.fetchall()
                if inv_antes==inv_desp:
                    print("No se ha encontrado el producto a eliminar.")
                    conexion.close()
                    return MenuFuncionarios.ejecutarMenuJefeventa()
                
                else:
                    conexion.commit()
                    print("Producto eliminado correctamente.")
                    conexion.close()
                    return MenuFuncionarios.ejecutarMenuJefeventa()
            else:
                print("Seleccione una opción válida.\n")
                return MenuFuncionarios.ejecutarMenuJefeventa()

        elif opcion==5:
            codprod=int(input("\nIngrese el Codigo del producto que desea modificar: "))
            conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
            cursor = conexion.cursor()
            sql0 = f"select * from inventario where cod_prod = '{codprod}'"
            cursor.execute(sql0)
            producto = cursor.fetchall()
            print(producto)
            print("Si este es el producto que desea modificar, escriba 1. Si no, precione cualquier otro NÚMERO.\n")
            opcion=int(input())
            
            if opcion==1:
                print("\nIngrese los nuevos datos del producto:\n")
                nombre=input("Nombre del producto: ")
                stock=int(input("Stock disponible: "))
                precio=int(input("Precio del producto: "))
                sql1 = f"select * from categorias"
                cursor.execute(sql1)
                cat = cursor.fetchall()
                print("\nCategorías disponibles:")
                print("\nId Categoría | Nombre de la categoría | Descripción de la categoría")
                print(cat)
                idcategoria=int(input("Id categoría: "))
                sql = f"UPDATE `inventario` SET `nom_prod`='{nombre}',`stock_prod`= '{stock}' ,`precio_prod`= '{precio}',`idcategorias`= '{idcategoria}' WHERE cod_prod = '{codprod}'"
                cursor.execute(sql)
                conexion.commit()
                print("Producto modificado.")
                conexion.close()
                return MenuFuncionarios.ejecutarMenuJefeventa()
            
            else:
                return MenuFuncionarios.ejecutarMenuJefeventa()

        elif opcion==6:
            conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
            cursor = conexion.cursor()
            print("\nInserte los datos del Nuevo vendedor:")
            nombre=input("Nombre: ")
            apellido=input("Apellido: ")
            rut=input("Rut: ")
            telefono=input("Telefono: ")
            direccion=input("Dirección: ")
            correo=input("Correo electrónico: ")
            contra=input("Contraseña de inicio de sesión: ")
            sql = f"insert into personas values(null,'{rut}','{nombre}','{apellido}','{telefono}','{direccion}','{correo}','{contra}',1)"
            cursor.execute(sql)
            conexion.commit()
            conexion.close()
            print("\nSe ha ingresado el vendedor con éxito.\n")
            return MenuFuncionarios.ejecutarMenuJefeventa()

        elif opcion==7:
            conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
            cursor = conexion.cursor()
            sql0 = f"select * from personas"
            cursor.execute(sql0)
            personas_ant = cursor.fetchall()
            print("\nInserte los datos del vendedor que desea eliminar:")
            nombre=input("Nombre: ")
            rut=input("Rut: ")
            sql = f"delete from personas where rut = '{rut}' and nombre_persona = '{nombre}'"
            cursor.execute(sql)
            sql1 = f"select * from personas"
            cursor.execute(sql1)
            personas_desp = cursor.fetchall()
            if personas_ant==personas_desp:
                print("No se ha encontrado la persona a eliminar.")
                conexion.close()
                return MenuFuncionarios.ejecutarMenuJefeventa()
                
            else:
                conexion.commit()
                print("Persona eliminada correctamente.")
                conexion.close()
                return MenuFuncionarios.ejecutarMenuJefeventa()
            
        elif opcion==8:
            idperson=int(input("\nIngrese el Id de la persona que desea modificar: "))
            conexion = mysql.connector.connect(database="sistema_de_ventas", user="root")
            cursor = conexion.cursor()
            sql0 = f"select * from personas where idpersona = '{idperson}'"
            cursor.execute(sql0)
            producto = cursor.fetchall()
            print(producto)
            print("Si esta es la persona que desea modificar, escriba 1. Si no, precione cualquier otro NÚMERO.\n")
            opcion=int(input())
            
            if opcion==1:
                print("\nIngrese los nuevos datos de la persona:\n")
                rut_=input("Rut: ")
                nombr=(input("Nombre de la persona: "))
                apellid=(input("Apellido de la persona: "))
                telefon=int(input("Telefono: "))
                direccio=input("Dirección: ")
                corre=input("Correo electrónico: ")
                contr=input("Contraseña: ")
                sql = f"UPDATE `personas` SET rut ='{rut_}', nombre_persona ='{nombr}', apellido = '{apellid}' ,direccion = '{direccio}', email_user = '{corre}', password ='{contr}', idrol =1 WHERE idpersona = '{idperson}'"
                cursor.execute(sql)
                conexion.commit()
                print("Persona modificada.")
                conexion.close()
                return MenuFuncionarios.ejecutarMenuJefeventa()
            
            else:
                return MenuFuncionarios.ejecutarMenuJefeventa()
            
        elif opcion==9:
            conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
            cursor = conexion.cursor()
            sql = f"SELECT * FROM `personas` WHERE idrol = 1"
            cursor.execute(sql)
            lista=cursor.fetchall()
            conexion.commit()
            conexion.close()
            print("\nID Persona | Rut | Nombre | Apellido | Telefono | Dirección | Correo electrónico | Contraseña | Id rol\n")
            print(lista)
            return MenuFuncionarios.ejecutarMenuJefeventa()
            
        elif opcion==10:
            conexion = mysql.connector.connect(database= "sistema_de_ventas", user="root")
            cursor = conexion.cursor()
            sql0 = f"Select * from estado_jornada"
            cursor.execute(sql0)
            estado_ant=cursor.fetchall()
            print("\n1. Iniciar jornada diaria.")
            print("2. Terminar jornada diaria.")
            opcion=int(input("Ingrese una opción: "))
            if opcion==1:
                sql = f"update estado_jornada set estado = 1"
                cursor.execute(sql)
                sql2 = f"select * from estado_jornada"
                cursor.execute(sql2)
                estado_desp=cursor.fetchall()
                conexion.commit()
                if estado_ant==estado_desp:
                    print("El estado de la jornada ya estaba iniciado.")
                    cursor.close()
                    return MenuFuncionarios.ejecutarMenuJefeventa()

                else:
                    print("Se ha iniciado la jornada diaria.")
                    cursor.close()
                    return MenuFuncionarios.ejecutarMenuJefeventa()
            
            elif opcion==2:
                sql = f"update estado_jornada set estado = 0"
                cursor.execute(sql)
                sql2 = f"select * from estado_jornada"
                cursor.execute(sql2)
                estado_desp=cursor.fetchall()
                conexion.commit()
                if estado_ant==estado_desp:
                    print("El estado de la jornada ya estaba apagado.")
                    cursor.close()
                    return MenuFuncionarios.ejecutarMenuJefeventa()

                else:
                    print("Se ha finalizado la jornada diaria.")
                    cursor.close()
                    return MenuFuncionarios.ejecutarMenuJefeventa()
            
            else:
                print("Debe seleccionar una opción válida.")
                cursor.close()
                return MenuFuncionarios.ejecutarMenuJefeventa()

        else:
            input("Error, debe ingresar una opción válida.")
            return MenuFuncionarios.ejecutarMenuJefeventa()
            
    def ejecutarMenuVendedor(vendedor):
        print ("\nBienvenido al Sistema ", vendedor.nombre)
        print ("M E N Ú")
        print ("--------------------------")
        print ("1. Agregar Venta")
        print ("2. Buscar Producto")
        print ("3. Listar Productos")
        print ("\nSeleccione una opción:\n")
        opcion=int(input())        

        if opcion==1:
            if estadoJornada()==1:
                pedido= generarPedido(vendedor)
                while True:
                    busqueda=input("Ingrese el producto: \n")
                    producto=buscarProducto(busqueda)
                    cantidad=int(input("Ingrese cantidad: \n"))
                    agregarAlCarro(pedido,producto,cantidad)
                    repetir=input("¿Desea agregar otro producto? SI[s] / NO[n] \n")
                    if repetir=="s":
                        True
                    else:
                        break

                tipo_doc=int(input("Seleccione tipo de documento\n [1] Boleta \n [2] Factura \n"))
                if tipo_doc==1:
                    boleta = generarBoleta(pedido)
                    vistaPrevia(boleta,1)
                    print("=========================================================================")
                    print("")
                    if int(input("¿Desea volver al menú? \n1. Si\n2. No\n"))==1:
                        return MenuFuncionarios.ejecutarMenuVendedor(vendedor)
                    else:
                        return print("Has cerrado la sesión.")    
                elif tipo_doc==2:
                    factura=generarFactura(pedido)
                    vistaPrevia(factura,2)
                    print("=========================================================================")
                    print("")
                    if int(input("¿Desea volver al menú? \n1. Si\n2. No\n"))==1:
                        return MenuFuncionarios.ejecutarMenuVendedor(vendedor)
                    else:
                        return print("Has cerrado la sesión.")
            else:
                input("La jornada aún no comienza. El Jefe de Ventas debe iniciarla. Presione cualquier tecla para volver.")
                return MenuFuncionarios.ejecutarMenuVendedor(vendedor)
        elif opcion==2:
            busqueda=input("Ingrese código o nombre de producto: \n")
            producto=buscarProducto(busqueda)
            print("Resultado de busqueda:\n \n")
            print("Código de producto:\n        ",producto.cod_prod)
            print("Nombre del producto:\n        ",producto.nom_prod)
            print("Precio unitario:\n        ",producto.valor)
            print("\n \n")
            if int(input("¿Desea volver al menú? \n1. Si\n2. No\n"))==1:
                return MenuFuncionarios.ejecutarMenuVendedor(vendedor)
            else:
                return print("Has cerrado la sesión.")
        elif opcion==3:
            mostrarProductos()
            print("\n \n")
            if int(input("¿Desea volver al menú? \n1. Si\n2. No\n"))==1:
                return MenuFuncionarios.ejecutarMenuVendedor(vendedor)
            else:
                return print("Has cerrado la sesión.")
#MenuFuncionarios.ejecutarMenuVendedor(Vendedor(1,"9766975-6","Rodrigo","Rosales",91924488,"Serena 123","rod_ros@gmail.com","RodROSS321"))
