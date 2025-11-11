import streamlit as st
from models.producto import Producto, Carrito

st.title("7) Composición")

st.write("""
En la **composición**, un objeto contiene a otros objetos y delega tareas.  
El `Carrito` **compone** varios `Producto`.  
Si destruimos el carrito, se destruyen sus productos (relación *“tiene un”*).
""")

p1 = Producto("Mouse", 50)
p2 = Producto("Teclado", 80)
carrito = Carrito()
carrito.agregar(p1)
carrito.agregar(p2)

st.subheader("Productos en el carrito:")
for linea in carrito.listar():
    st.write("-", linea)

st.success(f"Total: ${carrito.total():.2f}")

st.code("""
class Carrito:
    def __init__(self):
        self.items = []  # Composición: contiene objetos Producto
""", language="python")
