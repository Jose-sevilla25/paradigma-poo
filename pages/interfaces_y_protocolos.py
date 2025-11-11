import streamlit as st
from abc import ABC, abstractmethod

st.title("6) Interfaces y Protocolos")

st.write("""
En Python usamos **clases abstractas** o **protocolos** para definir contratos.  
No obligan a una implementación concreta, pero sí a una **interfaz común**.
""")

# --- Ejemplo simple ---
class Enviable(ABC):
    @abstractmethod
    def enviar(self):
        pass

class Email(Enviable):
    def enviar(self):
        return "📧 Enviando correo electrónico..."

class SMS(Enviable):
    def enviar(self):
        return "📱 Enviando mensaje SMS..."

tipo = st.selectbox("Tipo de envío", ["Email", "SMS"])
obj = Email() if tipo == "Email" else SMS()

if st.button("Enviar"):
    st.success(obj.enviar())

st.code("""
from abc import ABC, abstractmethod

class Enviable(ABC):
    @abstractmethod
    def enviar(self):
        pass

class Email(Enviable):
    def enviar(self):
        return "Enviando correo..."
""", language="python")
