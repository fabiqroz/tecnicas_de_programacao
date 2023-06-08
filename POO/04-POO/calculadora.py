''' Criando um módulo chamado calculadora:
Módulo de cálculo que faz operações matemáticas simples, 
como adição, multiplicação, subtração e divisão.'''


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


## Com POO:

class calculadora():
    # construtor
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num1
    
    # metodo soma
    def som(self):
        return self.a + self.b
    
    # metodo subtracao
    def dif(self):
        return self.a - self.b
    
    # metodo multiplicacao
    def mul(self):
        return self.a * self.b
    
    #metodo divisao
    def div(self):
        return self.a / self.b