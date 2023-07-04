# Ordenacao e arrays

n = int(input())

nomes = []
comportados = 0

for i in range(n):
    comp, nome = input().split()
    nomes.append(nome)
    
    if comp == '+':
        comportados += 1

nomes.sort()

for nome in nomes:
    print(nome)

print(f'Se comportaram: {comportados} | Nao se comportaram: {n-comportados}')