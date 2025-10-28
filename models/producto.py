# models/producto.py
from dataclasses import dataclass

class Producto:
    """
    Clase base para todos los productos.
    - nombre (público)
    - _precio (protegido por convención)
    - __costo_base (privado por name mangling, solo para demo de visibilidad)
    """
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self._precio = 0.0           # "protegido" (convención)
        self.precio = precio         # usa property para validar
        self.__costo_base = 0.0      # "privado" (name mangling)

    # --- Encapsulamiento: property con validación ---
    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, value: float):
        if value < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = float(value)

    # Solo para mostrar visibilidad (lectura del 'privado')
    def obtener_costo_base(self) -> float:
        return self.__costo_base

    def asignar_costo_base(self, valor: float):
        if valor < 0:
            raise ValueError("El costo base no puede ser negativo.")
        self.__costo_base = float(valor)

    # --- Punto de extensión polimórfico ---
    def precio_final(self) -> float:
        """Por defecto, el precio final es el precio."""
        return self.precio

    def descripcion(self) -> str:
        return f"{self.nombre} (${self.precio:.2f})"

class ProductoFisico(Producto):
    def __init__(self, nombre: str, precio: float, costo_envio: float = 0.0):
        super().__init__(nombre, precio)
        self.costo_envio = max(0.0, float(costo_envio))

    def precio_final(self) -> float:
        # envío se suma al precio
        return self.precio + self.costo_envio

    def descripcion(self) -> str:
        return f"{self.nombre} (Físico) ${self.precio_final():.2f} (incluye envío)"

class ProductoDigital(Producto):
    def __init__(self, nombre: str, precio: float, descuento: float = 0.10):
        super().__init__(nombre, precio)
        # descuento 0..1
        self.descuento = min(max(descuento, 0.0), 1.0)

    def precio_final(self) -> float:
        # aplica descuento por distribución digital
        return self.precio * (1 - self.descuento)

    def descripcion(self) -> str:
        return f"{self.nombre} (Digital) ${self.precio_final():.2f} (con descuento)"

# Un carrito mínimo para usar en polimorfismo
@dataclass
class Item:
    producto: Producto
    cantidad: int = 1

class Carrito:
    def __init__(self):
        self.items: list[Item] = []

    def agregar(self, producto: Producto, cantidad: int = 1):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        self.items.append(Item(producto, cantidad))

    def total(self) -> float:
        return sum(it.producto.precio_final() * it.cantidad for it in self.items)

    def listar(self) -> list[str]:
        return [f"{it.cantidad} x {it.producto.descripcion()}" for it in self.items]
