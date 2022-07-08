from dataclasses import dataclass

@dataclass

class inventario:
    cod_prod: int
    nom_prod: str
    stock_prod: int
    precio_prod: int
    descripcion_prod: str
    idcategorias: int