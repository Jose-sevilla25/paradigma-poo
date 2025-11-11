# models/decoradores.py
from models.producto import Producto

class ProductoDecorator(Producto):
    """Clase base para decoradores de productos."""
    def __init__(self, producto: Producto):
        self._producto = producto

    def precio_final(self) -> float:
        return self._producto.precio_final()

    def descripcion(self) -> str:
        return self._producto.descripcion()

class ProductoConDescuento(ProductoDecorator):
    def __init__(self, producto: Producto, descuento: float):
        super().__init__(producto)
        self.descuento = descuento

    def precio_final(self) -> float:
        return self._producto.precio_final() * (1 - self.descuento)

    def descripcion(self) -> str:
        return f"{self._producto.descripcion()} + descuento {self.descuento*100:.0f}%"

class ProductoConGarantia(ProductoDecorator):
    def __init__(self, producto: Producto, costo_garantia: float):
        super().__init__(producto)
        self.costo_garantia = costo_garantia

    def precio_final(self) -> float:
        return self._producto.precio_final() + self.costo_garantia

    def descripcion(self) -> str:
        return f"{self._producto.descripcion()} + garantía ${self.costo_garantia:.2f}"
