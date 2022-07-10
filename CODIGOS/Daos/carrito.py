from CODIGOS.Daos.DAOclientes import verificarCliente
from DAOdetalle_pedido_productos import *
from DAOinventario import *
from DAOpedido_ventas import *
from DAOclientes import *


import math

#devuelve ultimo id de pedido:int
def obtenerUltimoIDPedido():
    lista=listarIDsPedidos()
    return lista[len(lista)-1]

#imprime todos los productos del sistema con codigo y nombre
def mostrarProductos():
    productos=listarProductos()
    for producto in productos:
        print(producto+1,".  ",productos[producto][0]," --- ",productos[producto][1])
    return

#devuelve Producto
def buscarProducto(busqueda):
    return obtenerProducto(busqueda)

def generarPedido(vendedor):
    pedido = Pedido(obtenerUltimoIDPedido()+1,vendedor,list())
    insertarPedido(pedido)
    return pedido

def agregarAlCarro(pedido,producto,cantidad):
    id_detalle=insertarDetalle(pedido.idpedido,producto.cod_prod,cantidad)
    pedido.detalle.append(id_detalle)
    return

def calcularIVA(valor):
    return math.ceil(valor*0.19)

def obtenerPrecioProducto(cod_prod):
    producto=obtenerProducto(cod_prod)
    return producto.valor

def obtenerSubtotalProducto(iddt):
    detalle=obtenerDetallePedido(iddt)
    valor_unidad=obtenerPrecioProducto(detalle.cod_prod)
    return detalle.cantidad*valor_unidad

def obtenerSubtotalNeto(pedido):
    subtotal=0
    for iddt in range(len(pedido.detalle)):
        subtotal=subtotal+ obtenerSubtotalProducto(pedido.detalle[iddt])
    return subtotal

def generarBoleta(pedido):
    subtotal_neto=obtenerSubtotalNeto(pedido)
    total=subtotal_neto+calcularIVA(subtotal_neto)
    actualizarPedido(pedido.idpedido,total,1,0)
    return Boleta(pedido,total)

#retorna objeto cliente
def existeCliente(rut):
    if verificarCliente(rut)==1:
        return True
    else:
        return False

def generarFactura(pedido:Pedido):
    rut=int(input("Ingrese rut de cliente, sin puntos ni guion\n"))
    if existeCliente(rut):
        cliente=obtenerCliente(rut)
    else:
        print("El rut ingresado no está registrado como cliente. Agregue los datos a continuación para registrarlo:")
        razon=input("Ingrese Razón Social \n")
        giro=input("Ingrese Giro \n")
        direccion=input("Ingrese dirección \n")
        cliente=insertarCliente(rut,razon,giro,direccion)
    neto=obtenerSubtotalNeto(pedido)
    iva=calcularIVA(neto)
    total=neto+iva
    actualizarPedido(pedido.idpedido,total,2,cliente.rut)
    return Factura(pedido,cliente,neto,iva,total)

def imprimirDetalleBoleta(boleta:Boleta):
    print("        Código de Producto -- Producto -- Cantidad -- Valor unidad -- Subtotal")
    print("        -----------------------------------------------------------------------")
    for i in boleta.pedido.detalle:
        detalle=obtenerDetallePedido(i)
        producto=obtenerProducto(detalle.cod_prod)
        print("        ",detalle.cod_prod," -- ",producto.nom_prod," -- ",detalle.cantidad," -- ",producto.valor," -- ",detalle.cantidad*producto.valor)
    return

def imprimirDetalleFactura(factura:Factura):
    print("        Código de Producto -- Producto -- Cantidad -- Valor unidad -- Subtotal Neto -- IVA -- Subtotal + IVA")
    print("        -----------------------------------------------------------------------------------------------------")
    for i in factura.pedido.detalle:
        detalle=obtenerDetallePedido(i)
        producto=obtenerProducto(detalle.cod_prod)
        print("        ",detalle.cod_prod," -- ",producto.nom_prod," -- ",detalle.cantidad," -- ",producto.valor," -- ",detalle.cantidad*producto.valor," -- ",calcularIVA(detalle.cantidad*producto.valor)," -- ",(detalle.cantidad*producto.valor)+calcularIVA(detalle.cantidad*producto.valor))


def vistaPrevia(documento,tipo_documento):
    if tipo_documento==1:
        print("VISTA PREVIA DE LA BOLETA\n")
        print("----------------------------")
        print("Pedido Nro: ",documento.pedido.idpedido)
        print("Vendedor: ",documento.pedido.vendedor.nombre)
        print("Detalle de Productos\n+++++++++++++++++++++++")
        imprimirDetalleBoleta(documento)
        print("+++++++++++++++++++++++")
        print("Total a pagar: ",documento.total)
    elif tipo_documento==2:
        print("VISTA PREVIA DE LA FACTURA\n")
        print("----------------------------")
        print("Pedido Nro: ",documento.pedido.idpedido)
        print("Vendedor: ",documento.pedido.vendedor.nombre)
        print("Detalle de Productos\n+++++++++++++++++++++++")
        imprimirDetalleFactura(documento)
        print("+++++++++++++++++++++++")
        print("Total Neto: ",documento.neto)
        print("IVA: ",documento.iva)
        print("Total a pagar: ",documento.total)
    return