from dataclasses import dataclass
from datetime import datetime

@dataclass
class Producto:
    cod_prod: int
    nom_prod: str
    valor: int

@dataclass
class Tipo_doc:
    iddoc: int
    tipo_documento: str

@dataclass
class Pedido:
    idpedido: int
    vendedor: int
    detalle: list

@dataclass
class Boleta:
    pedido:int
    total:int

@dataclass
class Factura:
    pedido:int
    rut_cliente:int
    giro:str
    direccion:str
    neto:int
    iva:int
    total:int

@dataclass
class Registro_detalle:
    iddt: int
    cod_prod: int
    idpedido: int
    cantidad: int

@dataclass
class Vendedor:
    id: int
    rut: str
    nombre: str
    apellido: str
    telefono: int
    direccion: str
    email_user: str
    password: str

@dataclass
class Cliente:
    rut: str
    nombre: str
    apellido: str
    direccion: str
    telefono: int

