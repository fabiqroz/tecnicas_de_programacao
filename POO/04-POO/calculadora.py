''' Criando um módulo chamado calculadora:
Módulo de cálculo que faz operações matemáticas simples, 
como adição, multiplicação, subtração e divisão.'''


## Com POO:

class calculadora():
    # construtor
    def __init__(self):
       self.som = 0
       self.dif = 0
       self.mul = 0
       self.div = 0
    
    # metodo soma
    def soma(self, a, b):
        self.som = a + b
        return self.som
    
    # metodo subtracao
    def subtrai(self, a, b):
        self.dif = a - b
        return self.dif
    
    # metodo multiplicacao
    def multiplica(self, a, b):
        self.mul = a * b
        return self.mul
    
    #metodo divisao
    def divide(self, a, b):
        self.div = a/b
        return self.div
    

# Sem POO:

# funcao soma
def som(a,b):
    return a + b

# funcao diferenca
def dif(a,b):
    return a - b

# funcao multiplicacao
def mul(a,b):
    return a * b

# funcao divisao
def div(a,b):
    return a / b