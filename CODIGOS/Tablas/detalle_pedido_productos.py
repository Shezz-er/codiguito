from dataclasses import dataclass

@dataclass

class detalle_pedido_productos:
    iddt: int
    cod_prod: int
    idpedido: int
    cantidad: int