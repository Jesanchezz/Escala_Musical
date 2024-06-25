from abc import ABC, abstractmethod

class EscalaMusical(ABC):
    
    @abstractmethod
    def crear_escala_mayor(self):
        pass

    @abstractmethod
    def crear_escala_menor(self):
        pass