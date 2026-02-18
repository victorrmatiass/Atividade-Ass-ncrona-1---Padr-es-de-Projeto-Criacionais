from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass

class Caminhao(Transporte):
    def entregar(self):
        return "Entrega feita por terra em uma caixa."

class Navio(Transporte):
    def entregar(self):
        return "Entrega feita pelo mar em um container."

class Logistica(ABC):
    @abstractmethod
    def criar_transporte(self) -> Transporte:
        pass

    def planejar_entrega(self):
        transporte = self.criar_transporte()
        resultado = transporte.entregar()
        print(f"Logística: O plano foi executado -> {resultado}")

class LogisticaViaria(Logistica):
    def criar_transporte(self) -> Transporte:
        return Caminhao()

class LogisticaMaritima(Logistica):
    def criar_transporte(self) -> Transporte:
        return Navio()


def codigo_cliente(logistica: Logistica):
    logistica.planejar_entrega()

print("App: Iniciando com Logística Viária.")
codigo_cliente(LogisticaViaria())

print("\nApp: Iniciando com Logística Marítima.")
codigo_cliente(LogisticaMaritima())