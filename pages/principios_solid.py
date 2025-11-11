import streamlit as st
from models.producto import ProductoFisico, ProductoDigital
from models.solid_demo import CalculadoraSinSOLID, CalculadoraConSOLID, ImpuestoIVA, ImpuestoReducido

st.title("10) Principios SOLID")

st.write("""
Los principios **SOLID** mejoran la mantenibilidad y extensibilidad del código.
A continuación se comparan ejemplos sin y con SOLID.
""")

productos = [
    ProductoFisico("Monitor", 200, 10),
    ProductoDigital("Ebook", 50, 0.2)
]

modo = st.radio("Modo", ["Sin SOLID", "Con SOLID"])

if modo == "Sin SOLID":
    calc = CalculadoraSinSOLID()
    total = calc.calcular_total(productos)
    st.warning(f"Total calculado (mezcla responsabilidades): ${total:.2f}")
else:
    iva = st.selectbox("Tipo de impuesto", ["IVA 21%", "Reducido 10%"])
    estrategia = ImpuestoIVA() if iva == "IVA 21%" else ImpuestoReducido()
    calc = CalculadoraConSOLID(estrategia)
    total = calc.calcular_total(productos)
    st.success(f"Total con SOLID aplicado: ${total:.2f}")

st.code("""
class CalculadoraConSOLID:
    def __init__(self, estrategia_impuesto):
        self.estrategia_impuesto = estrategia_impuesto

    def calcular_total(self, productos):
        subtotal = sum(p.precio_final() for p in productos)
        return subtotal + self.estrategia_impuesto.aplicar(subtotal)
""", language="python")
