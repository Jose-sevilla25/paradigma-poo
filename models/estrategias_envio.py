# models/estrategias_envio.py
from abc import ABC, abstractmethod

class EstrategiaEnvio(ABC):
    @abstractmethod
    def calcular_envio(self, subtotal: float) -> float:
        pass

class EnvioEstandar(EstrategiaEnvio):
    def calcular_envio(self, subtotal: float) -> float:
        return 10.0 if subtotal < 100 else 0.0

class EnvioExpress(EstrategiaEnvio):
    def calcular_envio(self, subtotal: float) -> float:
        return subtotal * 0.10

class RetiroSucursal(EstrategiaEnvio):
    def calcular_envio(self, subtotal: float) -> float:
        return 0.0
