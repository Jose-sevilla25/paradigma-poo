# models/solid_demo.py
# Ejemplo simple de aplicar principios SOLID

# --- Sin SOLID ---
class CalculadoraSinSOLID:
    def calcular_total(self, productos):
        total = 0
        for p in productos:
            total += p.precio_final()
        print("Total:", total)  # Violación SRP (calcula + muestra)
        return total

# --- Con SOLID ---
# S: Single Responsibility -> cada clase hace una cosa
# O: Open/Closed -> nuevas estrategias sin modificar código viejo
# D: Dependency Inversion -> depende de abstracciones

class CalculadoraConSOLID:
    def __init__(self, estrategia_impuesto):
        self.estrategia_impuesto = estrategia_impuesto

    def calcular_subtotal(self, productos):
        return sum(p.precio_final() for p in productos)

    def calcular_total(self, productos):
        subtotal = self.calcular_subtotal(productos)
        return subtotal + self.estrategia_impuesto.aplicar(subtotal)

# Ejemplo de “inyección” de estrategia (O y D)
class ImpuestoIVA:
    def aplicar(self, subtotal):
        return subtotal * 0.21

class ImpuestoReducido:
    def aplicar(self, subtotal):
        return subtotal * 0.10
