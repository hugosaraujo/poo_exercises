# 1- Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos. 
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


carro1 = Carro('Tempra', 'Preta', 1998)

# 2- Crie uma classe chamada Restaurante com os atributos nome, categoria e ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
"""
class Restaurante:
    nome = nome
    categoria = categoria
    ativo = True
    endereco = ''
    avaliacao = 0
""" 
# 3-  Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria e inicia o status como False por padrão. Crie uma instância utilizando o construtor. 
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        status = False
        endereco = ''
        avaliacao = 0


# 4- Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.    
    def __str__(self):
        return f'O restaurante {self.nome} é do tipo {self.categoria}'


gula = Restaurante('Gula', 'Brasileira')
gula.endereco = 'Rua dos Bobos, 0'
gula.avaliacao = 4.5
print(gula)



# 5- Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente: 
    def __init__(self, nome, idade, sexo, email):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.email = email 

cliente1 = Cliente('João', 25, 'M', 'jao@email.com')
cliente2 = Cliente('Maria', 30, 'F', 'mariadascouves22@gmail.com')
cliente3 = Cliente('Cleiton', 35, 'M', 'cleitin.das.operacoes@bol.com')