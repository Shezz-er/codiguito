from dataclasses import dataclass
from datetime import datetime

@dataclass

class pedido_ventas:
    idpedido: int
    idpersona: int
    fecha: datetime
    monto: int
    iddoc: int
    #rut cliente
    #id detalle