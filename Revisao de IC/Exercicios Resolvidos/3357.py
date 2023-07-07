# Revisao IC - arrays e funções

def encontra_rica(n, l, q, nomes):
    
    rodadas = int(l//q)
    sobra = ((l*10)%(q*10))/10

    if sobra != 0:
        rica = nomes[rodadas%len(nomes)]
        bebeu = sobra
    else:
        rica = nomes[rodadas%len(nomes)-1]
        bebeu = q
    
    return rica, bebeu

# Fluxo principal do programa
n, litros_garrafa, litros_cuia = [eval(num) for num in input().split()]

nomes = []
[nomes.append(nome) for nome in input().split()]


rica, bebeu = encontra_rica(n, litros_garrafa, litros_cuia, nomes)

print(f'{rica} {bebeu:.1f}')
    
