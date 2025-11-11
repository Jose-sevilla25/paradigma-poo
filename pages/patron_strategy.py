import streamlit as st
from models.estrategias_envio import EnvioEstandar, EnvioExpress, RetiroSucursal
from models.producto import ProductoFisico, Carrito

st.title("8) Patrón Strategy")

st.write("""
**Strategy** permite cambiar el algoritmo sin modificar el código del cliente.  
Acá el envío del carrito se calcula con distintas estrategias intercambiables.
""")

estrategias = {
    "Estandar": EnvioEstandar(),
    "Express": EnvioExpress(),
    "Retiro en Sucursal": RetiroSucursal()
}

nombre = st.selectbox("Estrategia de envío", list(estrategias.keys()))
estrategia = estrategias[nombre]

# Demo
carrito = Carrito()
carrito.agregar(ProductoFisico("Libro", 50, 10))
subtotal = carrito.total()
costo_envio = estrategia.calcular_envio(subtotal)
total = subtotal + costo_envio

st.write(f"Subtotal: ${subtotal:.2f}")
st.write(f"Estrategia '{nombre}' → Envío: ${costo_envio:.2f}")
st.success(f"Total final: ${total:.2f}")

st.code("""
class EnvioEstandar(EstrategiaEnvio):
    def calcular_envio(self, subtotal):
        return 10.0 if subtotal < 100 else 0.0
""", language="python")
