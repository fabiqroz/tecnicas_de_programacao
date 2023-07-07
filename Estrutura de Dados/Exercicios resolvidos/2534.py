import numpy as np

def cadastra_notas(n):
    notas = np.empty(n, dtype='int')
    
    for i in range(n):
        notas[i] = int(input())
    
    notas.sort()
    notas = np.flip(notas)
    
    return notas

def consulta(n, notas): 
    consultas = np.empty(n, dtype='int')
    for i in range(n):
        consultas[i] = notas[int(input())-1]
    
    return consultas

# Fluxo principal do programa
entradas = [int(i) for i in input().split()]

n_habitantes = entradas[0]
n_consultas = entradas[1]

notas = cadastra_notas(n_habitantes)
resultado_consultas = consulta(n_consultas, notas)

[print(nota) for nota in resultado_consultas]



