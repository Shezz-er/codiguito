from dataclasses import dataclass

@dataclass
class Vendedor:
    _id: int
    _rut: str
    _nombre: str
    _apellido: str
    _telefono: int
    _direccion: str
    _email_user: str
    _password: str

@dataclass
class Cliente:
    _rut: int
    _razon: str
    _giro: str
    _direccion: str

@dataclass
class Producto:
    _cod_prod: int
    _nom_prod: str
    _valor: int

@dataclass
class Tipo_doc:
    _iddoc: int
    _tipo_documento: str

@dataclass
class Pedido:
    _idpedido: int
    _vendedor: Vendedor
    _detalle: list

@dataclass
class Boleta:
    _pedido:Pedido
    _total:int

@dataclass
class Factura:
    _pedido:Pedido
    _cliente:Cliente
    _neto:int
    _iva:int
    _total:int

@dataclass
class Registro_detalle:
    _iddt: int
    _cod_prod: int
    _idpedido: int
    _cantidad: int

@dataclass
class Login:
    _id:int
    _password:str

@dataclass
class Persona:
    _idpersona: int
    _rut: str
    _nombre_persona: str
    _apellido: str
    _telefono: int
    _direccion: str
    _email_user: str
    _password: str
    _idrol: int
