from abc import ABC, abstractmethod
from main import NoContieneCaracterEspecial, NoContieneMayuscula, NoContieneMinuscula, NoContieneNumero, NoCumpleCalisto



class ReglaValidacion(ABC):
    
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada    
    
    def _validar_longitud(self, clave: str):
        return len(clave) >= self.longitud_esperada
    
    def _contiene_mayuscula (self, clave: str)-> bool:
        return any(caracter.isupper() for caracter in clave)
    
    def _contiene_minuscula (self, clave: str)-> bool:
        return any(caracter.islower() for caracter in clave)
    
    def _contiene_numero (self, clave: str)-> bool:
        return any(caracter.isdigit() for caracter in clave)    
    
    @abstractmethod
    def es_valida(self, clave: str)-> bool:
        pass
    
    
    
    
class ReglaValidacionCalisto(ReglaValidacion):
    
    def contiene_calisto(self, clave: str)->bool:
        pass
    
    def es_valida(self, clave: str)-> bool:
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_calisto(clave)
        return True







class ReglaValidacionGanimedes(ReglaValidacion):

    def contiene_caracter_especial(self, clave: str)->bool:
        caracteres_especiales = '@_#$%'
        return any(caracter in clave for caracter in caracteres_especiales)
    
    def es_valida(self, clave: str)-> bool:
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_caracter_especial(clave)
        return True





class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla
    
    def es_valida(self, clave: str)-> bool:
        return self.regla.es_valida(clave)