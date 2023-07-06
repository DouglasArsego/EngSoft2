from carros import Carro, CarroHonda, CarroToyota

# Registro protótipo
class RegistroPrototipo:
    prototipos = {} # Dicionário vazio para armazenar os protótipos

    # Adiciona protótipo ao registro
    @staticmethod
    def adicionar_prototipo(chave, prototipo):
        RegistroPrototipo.prototipos[chave] = prototipo

    # Recupera o protótipo do registro e realiza a clonagem
    @staticmethod
    def obter_clonagem(chave):
        prototipo = RegistroPrototipo.prototipos.get(chave)
        if prototipo:
            return prototipo.clonar()
        return None
    
    # Essa implementação do registro de protótipos permite adicionar protótipos
    # ao registro e obter clones desses protótipos posteriormente, com base em suas chaves.

# Exemplo de uso
if __name__ == '__main__':
    # Criando instâncias dos protótipos
    prototipo1 = CarroHonda(2020, "Civic", "Vermelho")
    prototipo2 = CarroToyota(2021, "Corolla", "Azul")

    # Adicionando protótipos ao registro
    RegistroPrototipo.adicionar_prototipo("HondaCivic2020", prototipo1)
    RegistroPrototipo.adicionar_prototipo("ToyotaCorolla2021", prototipo2)

    # Clonando os protótipos a partir do registro
    prototipo_clonado1 = RegistroPrototipo.obter_clonagem("HondaCivic2020")
    prototipo_clonado2 = RegistroPrototipo.obter_clonagem("ToyotaCorolla2021")

    # Verificando a clonagem
    if prototipo_clonado1:
        print("Protótipo Clonado 1 - Ano:", prototipo_clonado1._ano, "- Modelo:", prototipo_clonado1._modelo, "- Cor:", prototipo_clonado1._cor)

    if prototipo_clonado2:
        print("Protótipo Clonado 2 - Ano:", prototipo_clonado2._ano, "- Modelo:", prototipo_clonado2._modelo, "- Cor:", prototipo_clonado2._cor)


    # Clonando um protótipo com um atributo adicional
    prototipo_clonado3 = RegistroPrototipo.obter_clonagem("HondaCivic2020")

    if prototipo_clonado3:
        prototipo_clonado3._cor = "Verde"  # Atribuindo uma nova cor
        prototipo_clonado3._edicao = "Colecionador"  # Atribuindo um valor ao atributo adicional "edicao"

        # Verificando a clonagem
        print("Protótipo Clonado 3 - Ano:", prototipo_clonado3._ano, "- Modelo:", prototipo_clonado3._modelo, "- Cor:", prototipo_clonado3._cor, "- Edição:", prototipo_clonado3._edicao)
