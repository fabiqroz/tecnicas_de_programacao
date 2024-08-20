# Sem POO
pi = 3.1416 

def soma(a,b):
    return a+b

def diferenca(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

# Com POO

class calculadora():
    def __init__(self, a, b) -> None:
        self.pi = 3.1416
        self.num1 = a
        self.num2 = b

    def somar(self):
        return self.num1 + self.num2
    
    def subtrair(self):
        return self.num1 - self.num2
    
    def multiplicar(self):
        return self.num1 * self.num2
    
    def dividir(self):
        return self.num1 / self.num2
    