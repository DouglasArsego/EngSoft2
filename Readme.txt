Eng. Software 2 -  Doulgas Arsego

Infos:

main_Prototype.py - codigo com prototype
carros.py - codigo da classe/sub
main_sem_Prototype.py - codigo sem prototype


Padrão de Projeto Prototype - Material Explicativo

Descrição do Padrão

O padrão de projeto Prototype é um padrão criacional que permite a criação de novos objetos por meio da clonagem de um objeto protótipo existente. Ele fornece uma maneira de criar objetos duplicados, evitando a dependência de classes específicas e tornando o sistema mais flexível.

Estrutura do Padrão Neste Projeto

O padrão deste projeto Prototype envolve as seguintes entidades:
Carro: Classe base para as outras subclasses(Honda/Toyota). Ela possui um método clone que retorna uma cópia do objeto.
Registro de Protótipos: É uma parte de implementação do código (opcional) que mantém um conjunto de protótipos disponíveis. Ele permite adicionar protótipos ao registro e recuperar clones desses protótipos posteriormente, com base em suas chaves. O registro facilita o acesso aos protótipos e fornece uma forma padronizada de clonagem.

Pontos Fortes do Padrão

Facilidade na criação de objetos: O padrão Prototype permite criar objetos clonados sem depender de classes concretas. Isso oferece flexibilidade na criação de novos objetos com diferentes configurações.
Redução do acoplamento: O uso do padrão Prototype reduz o acoplamento entre o código cliente e os objetos protótipos. O cliente apenas precisa interagir com o registro de protótipos ou com os protótipos diretamente, sem depender de classes específicas.
Melhoria de desempenho: A clonagem de objetos através do padrão Prototype pode ser mais eficiente em termos de desempenho, em comparação com a criação de objetos a partir do zero. A clonagem evita a execução de lógicas complexas de inicialização de objetos, resultando em um desempenho aprimorado.
Extensibilidade: O padrão Prototype é facilmente extensível, permitindo a adição de novos protótipos ao registro de forma dinâmica. Isso torna o sistema mais escalável e facilita a incorporação de novos tipos de objetos.

Pontos Fracos do Padrão

Clonagem profunda: Uma das desvantagens do padrão Prototype é a necessidade de uma clonagem profunda dos objetos, especialmente se eles possuírem referências a outros objetos. A clonagem profunda garante que todos os objetos referenciados sejam copiados corretamente, mas pode exigir mais esforço de implementação.
Gerenciamento de registros: Se for utilizado um registro de protótipos, pode ser necessário gerenciar a adição e remoção adequada dos protótipos no registro. Isso pode adicionar complexidade ao código e requerer atenção adicional para garantir que os protótipos sejam manipulados corretamente.
Complexidade de implementação: O padrão Prototype pode aumentar a complexidade da implementação, especialmente quando se lida com objetos complexos e hierarquias de classes extensas.

Conclusões

O padrão de projeto Prototype é uma escolha adequada quando se deseja criar novos objetos com base em protótipos existentes. Ele fornece flexibilidade na criação de objetos e reduz o acoplamento entre o código cliente e as classes concretas.
Embora o padrão Prototype possua algumas desvantagens, como a necessidade de clonagem profunda e o gerenciamento de registros (neste caso), seus pontos fortes, como flexibilidade, redução do acoplamento e melhoria de desempenho, tornam-no uma opção viável em muitos cenários de desenvolvimento do software.
