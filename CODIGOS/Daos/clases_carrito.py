from dataclasses import dataclass

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
    rut: int
    razon: str
    giro: str
    direccion: str

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
    vendedor: Vendedor
    detalle: list

@dataclass
class Boleta:
    pedido:Pedido
    total:int

@dataclass
class Factura:
    pedido:Pedido
    cliente:Cliente
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
class Login:
    id:int
    password:str

@dataclass
class Persona:
    idpersona: int
    rut: str
    nombre_persona: str
    apellido: str
    telefono: int
    direccion: str
    email_user: str
    password: str
    idrol: int
