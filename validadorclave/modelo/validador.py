from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada
    
    def _validar_longitud(self, clave: str):
        return len(clave) >= self.longitud_esperada
    
    def _contiene_mayuscula (self, clave: str)-> bool:
        return any(caracter.isupper() for caracter in clave)
    
    def _contiene_minuscula (self, clave: str)-> bool:
        return any(caracter.islower() for caracter in clave)
    
    def _contiene_mayuscula (self, clave: str)-> bool:
        return any(caracter.isdigit() for caracter in clave)    
    
    @abstractmethod
    def es_valida(self, clave: str)-> bool:
        pass
    
    
class ReglaValidacionCalisto:
    
    def contiene_calisto(self, clave: str)->bool:
        pass

class ReglaValidacionGanimedes:
    def contiene_caracter_especial(self, clave: str)->bool:
        caracteres_especiales = '@_#$%'
        return any(caracter in clave for caracter in caracteres_especiales)

class Validador:
    pass