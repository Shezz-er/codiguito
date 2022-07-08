from DAOpedido_ventas import listarIDsPedidos
from clases_carrito import *
from DAOinventario import *
from DAOdetalle_pedido_productos import *
import math

#devuelve ultimo id de pedido:int
def obtenerUltimoIDPedido():
    lista=listarIDsPedidos()
    return lista[len(lista)-1]

#imprime todos los productos del sistema con codigo y nombre
def mostrarProductos():
    productos=listarProductos()
    for producto in productos:
        print(producto+1,".  ",productos[producto][0],"  ",productos[producto][1])
    return

#devuelve Producto
def buscarProducto(busqueda):
    return obtenerProducto(busqueda)


def generarPedido(vendedor):
    return Pedido(obtenerUltimoIDPedido()+1,vendedor,list())

def agregarAlCarro(pedido,producto,cantidad):
    id_detalle=insertarDetalle(pedido.idpedido,producto.cod_prod,cantidad)
    pedido.detalle.append(id_detalle)
    return

'''
def agregarProducto(pedido,cod_prod,cantidad):
    id_detalle=insertarDetalle(pedido.idpedido,cod_prod,cantidad)
    producto=obtenerProducto(cod_prod)
    if pedido.tipo_doc==1:
        detalle=obtenerDetalle(id_detalle)
        valor=producto.valor
        pedido.detalle.append(())

def buscarProducto(busqueda):
'''

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
    for i in pedido.detalle:
        subtotal=subtotal+ obtenerSubtotalProducto(i)
    total=subtotal+calcularIVA(subtotal)
    return Boleta(pedido,total)

def generarFactura():
    return

def emitirDocumento(pedido):
    return