n, l, q = [eval(num) for num in input().split()]

nomes = []
[nomes.append(nome) for nome in input().split()]


rodadas = int(l//q)
sobra = ((l*10)%(q*10))/10

if sobra != 0:
    rica = nomes[rodadas%len(nomes)]
    bebeu = sobra
else:
    rica = nomes[rodadas%len(nomes)-1]
    bebeu = q


print(f'{rica} {bebeu:.1f}')
    
