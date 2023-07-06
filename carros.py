from copy import deepcopy

# Classe base protótipo
class Carro:
    def __init__(self, ano, modelo):
        self._ano = ano
        self._modelo = modelo

    # Método de clonagem
    def clonar(self):
        return deepcopy(self)

# Subclasse protótipo 1
class CarroHonda(Carro):
    def __init__(self, ano, modelo, cor):
        super().__init__(ano, modelo)
        self._cor = cor

    # Sobrescreve o método de clonagem
    def clonar(self):
        return deepcopy(self)

# Subclasse protótipo 2
class CarroToyota(Carro):
    def __init__(self, ano, modelo, cor):
        super().__init__(ano, modelo)
        self._cor = cor

    # Sobrescreve o método de clonagem
    def clonar(self):
        return deepcopy(self)
