import streamlit as st
from models.producto import Producto

st.title("1) Clase y Objeto")

st.write("""
Una **clase** define la plantilla (atributos + métodos) y un **objeto** es una instancia concreta.
Acá instanciamos `Producto` y usamos su método.
""")

col1, col2 = st.columns(2)
with col1:
    nombre = st.text_input("Nombre", "Mouse")
with col2:
    precio = st.number_input("Precio", min_value=0.0, value=50.0, step=1.0)

p = Producto(nombre, precio)
st.success(f"Instancia creada → {p.descripcion()}")

st.code("""
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = 0.0
        self.precio = precio  # usa property para validar

    def descripcion(self):
        return f"{self.nombre} (${self.precio:.2f})"
""", language="python")
