from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada
    
    @abstractmethod
    def es_valida(self): 
        pass
    
    def _validar_longitud(self, clave) :
        return len(clave) >= self.longitud_esperada

        
class ReglaValidacionCalisto:
    pass

class ReglaValidacionGanimedes:
    pass
