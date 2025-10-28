import streamlit as st
from models.producto import Producto

st.title("3) Visibilidad")

st.write("""
Python no tiene modificadores `public/private/protected` como Java,  
pero usa **convenciones**:
- `publico` → sin guión bajo  
- `_protegido` → un guión bajo (no usar desde fuera, salvo necesidad)  
- `__privado` → *name mangling* (difícil de acceder por accidente)

Acá mostramos cómo acceder correctamente y qué pasa si forzamos el acceso.
""")

p = Producto("Lector USB", 30)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Acceso recomendado")
    st.write("- Público:", p.nombre)
    st.write("- Protegido (evitar):", p._precio)  # solo demo
    st.write("- Privado por método:", p.obtener_costo_base())

with col2:
    st.subheader("Acceso forzado (no recomendado)")
    st.write("Name mangling de __costo_base ⇒ _Producto__costo_base")
    try:
        valor = getattr(p, "_Producto__costo_base")
        st.warning(f"Acceso forzado a privado: {valor} (solo con fines educativos)")
    except AttributeError:
        st.success("No se pudo acceder al atributo privado.")

st.code("""
class Producto:
    def __init__(...):
        self.nombre = nombre      # público
        self._precio = 0.0        # 'protegido' por convención
        self.__costo_base = 0.0   # 'privado' (name mangling)
""", language="python")
