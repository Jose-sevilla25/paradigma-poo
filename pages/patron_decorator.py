import streamlit as st
from models.producto import ProductoFisico
from models.decoradores import ProductoConDescuento, ProductoConGarantia

st.title("9) Patrón Decorator")

st.write("""
**Decorator** permite agregar responsabilidades a un objeto **sin modificar su clase**.  
Acá un producto se envuelve con decoradores que añaden descuento o garantía.
""")

base = ProductoFisico("Silla Gamer", 200, costo_envio=20)
st.info(f"Base: {base.descripcion()} → ${base.precio_final():.2f}")

agregar_descuento = st.checkbox("Agregar descuento 10%")
agregar_garantia = st.checkbox("Agregar garantía $30")

decorado = base
if agregar_descuento:
    decorado = ProductoConDescuento(decorado, 0.10)
if agregar_garantia:
    decorado = ProductoConGarantia(decorado, 30)

st.success(f"Decorado: {decorado.descripcion()} → Total: ${decorado.precio_final():.2f}")

st.code("""
class ProductoConDescuento(ProductoDecorator):
    def precio_final(self):
        return self._producto.precio_final() * (1 - self.descuento)
""", language="python")
