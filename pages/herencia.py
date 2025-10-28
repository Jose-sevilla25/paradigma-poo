import streamlit as st
from models.producto import ProductoFisico, ProductoDigital

st.title("4) Herencia")

st.write("""
Creamos subclases a partir de `Producto`:  
- `ProductoFisico` agrega **costo de envío**.  
- `ProductoDigital` aplica **descuento**.
""")

tipo = st.selectbox("Tipo", ["Físico", "Digital"])
nombre = st.text_input("Nombre", "Auriculares")
precio = st.number_input("Precio base", min_value=0.0, value=100.0, step=1.0)

if tipo == "Físico":
    envio = st.number_input("Costo de envío", min_value=0.0, value=15.0, step=1.0)
    prod = ProductoFisico(nombre, precio, costo_envio=envio)
else:
    desc = st.slider("Descuento digital", min_value=0.0, max_value=0.5, value=0.10, step=0.05)
    prod = ProductoDigital(nombre, precio, descuento=desc)

st.success(f"{prod.descripcion()}  →  Precio final: ${prod.precio_final():.2f}")

st.code("""
class ProductoFisico(Producto):
    def __init__(..., costo_envio):
        super().__init__(nombre, precio)
        self.costo_envio = costo_envio

    def precio_final(self):
        return self.precio + self.costo_envio
""", language="python")
