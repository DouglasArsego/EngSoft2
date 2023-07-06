from carros import CarroHonda, CarroToyota

# Exemplo de uso
if __name__ == '__main__':
    # Criando instâncias dos carros concretos
    carro1 = CarroHonda(2020, "Civic", "Vermelho")
    carro2 = CarroToyota(2021, "Corolla", "Azul")

    # Criando clones dos carros
    carro_clonado1 = CarroHonda(carro1._ano, carro1._modelo, carro1._cor)
    carro_clonado2 = CarroToyota(carro2._ano, carro2._modelo, carro2._cor)

    # Verificando a clonagem
    if carro_clonado1:
        print("Carro Clonado 1 - Ano:", carro_clonado1._ano, "- Modelo:", carro_clonado1._modelo, "- Cor:", carro_clonado1._cor)

    if carro_clonado2:
        print("Carro Clonado 2 - Ano:", carro_clonado2._ano, "- Modelo:", carro_clonado2._modelo, "- Cor:", carro_clonado2._cor)
