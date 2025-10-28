import streamlit as st
from models.producto import ProductoFisico, ProductoDigital, Carrito

st.title("5) Polimorfismo y Despacho Dinámico")

st.write("""
**Mismo mensaje, distintas respuestas**.  
Llamamos a `precio_final()` sobre objetos de distintas clases y cada uno
resuelve **su propia implementación**.
""")

# Demo rápida: construimos un carrito con varios tipos
carrito = Carrito()

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Agregar Físico (Libro $50 + envío $8)"):
        carrito.agregar(ProductoFisico("Libro", 50, costo_envio=8))
with col2:
    if st.button("Agregar Digital (Curso $80 con 20%)"):
        carrito.agregar(ProductoDigital("Curso", 80, descuento=0.20))
with col3:
    if st.button("Agregar Físico (Mouse $40 + envío $10)"):
        carrito.agregar(ProductoFisico("Mouse", 40, costo_envio=10))

if carrito.items:
    st.subheader("Items")
    for linea in carrito.listar():
        st.write("•", linea)
    st.success(f"Total (suma polimórfica de precio_final): ${carrito.total():.2f}")
else:
    st.info("Agregá productos para ver el polimorfismo en acción.")

st.code("""
def total(self) -> float:
    return sum(it.producto.precio_final() * it.cantidad for it in self.items)
# ↑ Llamamos al mismo método 'precio_final()' y cada subclase responde distinto.
""", language="python")
