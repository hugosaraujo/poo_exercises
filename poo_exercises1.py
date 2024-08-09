class Restaurante:
    nome = ''
    categoria = ''
    status = False


# 1- Atribua o valor 'Italina' ao atributo da instancia restuarante_praca da classe Restaurante
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça Food'
restaurante_praca.categoria = 'Italiana'


# 2- Acesse o valor do atributo nome da instancia restaurante_praca da classe Restaurante
print(f'{restaurante_praca.nome} é do tipo {restaurante_praca.categoria}')


# 3 - Verifique o valor incial do atributo ativo para a instancia restaurante_praca da classe Restaurante e informe se o restaurante está ativo ou não
if restaurante_praca.status:
    print('Restaurante está ativo')
else:
    print('Restaurante está desativo')



# 4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria
categoria = Restaurante.categoria


# 5 - Altere o valor do atributo nome para "Bistrô"
restaurante_praca.nome = "Bistrô"


# 6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Planet'
restaurante_pizza.categoria = 'Fast Food'


# 7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'
if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food')
else: 
    print('Não é Fast Food')



# 8 - Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.status = True 


# 9 - Imprima no console o nome e a categoria da instância restaurante_praca. 
print(f'Restaurante: {restaurante_praca.nome} - Categoria: {restaurante_praca.categoria}')