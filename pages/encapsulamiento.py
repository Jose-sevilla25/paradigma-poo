import streamlit as st
from models.producto import Producto

st.title("2) Encapsulamiento")

st.write("""
Usamos **properties** para controlar el acceso a los atributos.
El setter de `precio` valida que el valor no sea negativo.
""")

nombre = st.text_input("Nombre", "Teclado")
precio = st.number_input("Precio (no negativo)", min_value=0.0, value=80.0, step=1.0)

p = Producto(nombre, precio)

st.info("Intentemos asignar un precio inválido (negativo).")
if st.button("Forzar precio = -10 (demostración)"):
    try:
        p.precio = -10
        st.error("No debería verse esto.")
    except Exception as e:
        st.success(f"Encapsulamiento funcionando: {e}")

st.write("Estado actual:", p.descripcion())

st.code("""
class Producto:
    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, value: float):
        if value < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = float(value)
""", language="python")
