from data_access.DAOdetalle_pedido_productos import *
from data_access.DAOinventario import *
from data_access.clases_carrito import *
from data_access.DAOpedido_ventas import *

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

def generarBoleta(pedido):
    subtotal=0
    for iddt in pedido.detalle:
        subtotal=subtotal+ obtenerSubtotalProducto(iddt)
    total=subtotal+calcularIVA(subtotal)
    actualizarPedido(pedido.idpedido,total,1,None)
    return Boleta(pedido,total)

def obtenerClienteRut(rut):
    #if consultarRut(rut)
    return

def generarFactura(pedido):
    return

def imprimirDetalleBoleta(boleta):
    print("        Código de Producto -- Producto -- Cantidad -- Valor unidad -- Subtotal")
    print("        -----------------------------------------------------------------------")
    for i in boleta.pedido.detalle:
        detalle=obtenerDetallePedido(i)
        producto=obtenerProducto(detalle.cod_prod)
        print("        ",detalle.cod_prod," -- ",producto.nom_prod," -- ",detalle.cantidad," -- ",producto.valor," -- ",detalle.cantidad*producto.valor)
    return



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
        imprimirDetalleBoleta(documento)
        print("+++++++++++++++++++++++")
