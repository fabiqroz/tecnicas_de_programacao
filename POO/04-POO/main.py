#from calculadora import soma, diferenca, multiplicacao, divisao
import calculadora as calc

numeros = [float(num) for num in input('Digite dois números reais separados por um espaço em branco: ').split()]

# s = calc.soma(numeros[0], numeros[1])
# d = calc.diferenca(numeros[0], numeros[1])
# m = calc.multiplicacao(numeros[0], numeros[1]
# dv = calc.divisao(numeros[0], numeros[1])

#from calculadora import calculadora

c = calc.calculadora(numeros[0], numeros[1])
s = c.somar()
d = c.subtrair()
m = c.multiplicar()
dv = c.dividir()

print(f'Soma: {s}, Diferença: {d}, Multiplicação: {m}, Divisão: {dv}')