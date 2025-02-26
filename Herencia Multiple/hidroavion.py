from volador import Volador
from navegable import Navegable

class Hidroavion(Volador,Navegable):
    def navegar(self):
        return super().navegar()
    def volar(self):
        return super().volar()
    
