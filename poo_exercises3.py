# 1- Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão. 
# 2- Na classe ContaBancaria, adicione um método especial __str__que retorne uma mensagem formatada com o titular e o saldo da conta. Crie duas instancias da classe e imprima essas instâncias.
# 3- Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo com TRUE. Crie uma instância da classe, chame o método e imprima o valor de ativo.
# 4- Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário. 
# 5- Crie uma instancia da classe e imprima o valor da propriedade ativo.
class ContaBancaria: 
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._status = False
        
    @classmethod
    def ativar_conta(cls,conta):
        conta._status = not conta._status
            


    def __str__(self):
        return f'Titular: {self._titular} - Saldo {self._saldo}'
    
conta1 = ContaBancaria('João', 1000)
conta2 = ContaBancaria('Rubens', 5000)

print(conta1)
print(conta2)

conta1.ativar_conta(conta1)
print(conta1._status) 


# 6- Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
# 7- Crie um método de classe para a classe ClienteBanco. 
class ClienteBanco:
    def __init__(self, nome, idade, sexo, email, profissao):
        self._nome = nome
        self._idade = idade
        self._sexo = sexo
        self._email = email
        self._profissao = profissao

    @classmethod
    def abrir_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta    

cliente1 = ClienteBanco('João', 25, 'M', 'jao@servidor.com', 'Programador')
cliente2 = ClienteBanco('Cleiton', 22, 'M', 'cleitinbomdeguerra@provedor.com', 'Soldado')
cliente3 = ClienteBanco('Sookie', 30, 'F', 'sookiestjames@starshollow.com', 'Chef de Cozinha')

conta_joao = ClienteBanco.abrir_conta('João', 1000)
