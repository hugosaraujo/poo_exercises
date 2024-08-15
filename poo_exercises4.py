# 1- Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão. 
# 2- Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o titulo, autor e ano de publicacao do livro. Crie duas instâncias da classe Livro e imprima essas instâncias. 
# 3- Adicione um método de instância chamado emprestar à classe Livro que define um atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não. 
# 4- Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'Titulo: {self._titulo} - Autor: {self._autor}, {self._ano_publicacao}'
    
    def emprestar(self): 
        self._disponivel = False

    @classmethod
    def listar_livros(cls):
        for livro in cls.livros:
            print(livro)

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._disponivel == True and livro._ano_publicacao == ano]
        if livros_disponiveis == []:
            print(f'Nenhum livro disponível para este ano')
        else: 
            print(f'Lista de livros disponíveis para o ano de {ano}:')
        for livro in livros_disponiveis:
            print(livro)
        

# 5- Crie um arquivo chamado biblioteca.py e importe a classe Livro nesse arquivo. 
# 6- No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo. 
# 7- Na biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico. 
# 8- Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str. 