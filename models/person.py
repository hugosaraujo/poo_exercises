class Person:
    def __init__(self, name, age=0, work=''):
        self._name = name
        self._age = age
        self._work = work

    def __str__(self):
        return f'{self._name} tem {self._age} anos e trabalha como {self._work}'
    
    def happy_birthday(self):
        self._age += 1

    @property
    def saudacao(self):
        labor = f'Olá, sou {self._name}! e trampo como {self._work}' if self._work else f'Olá, sou {self._name}!'
        return labor

person1 = Person('João', 25, 'Programador')
person2 = Person('Ana', 30, 'Analista de Sistemas')
person3 = Person('Maria', 35, 'Gerente de Projetos')

print(person1)
print(person2)
print(person3)

person1.happy_birthday()
person3.happy_birthday()

print(person1)
print(person2)
print(person3)

print(person2.saudacao)    