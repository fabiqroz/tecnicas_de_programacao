def ordena(lista):
    
    lista_ordenada = []
    tam = len(lista)

    for i in range(tam):
        maior = lista[0]
        for num in lista:
            if num > maior:
                maior = num
        
        lista_ordenada.append(maior)
        lista.remove(maior)
    
    return lista_ordenada

def eh_triangulo(lados):
    if lados[0] >= lados[1] + lados[2]:
        return True
    return False

def relacao_lados(lados):
    if lados[0]**2 == (lados[1]**2 + lados[2]**2):
        tipo = 'TRIANGULO RETANGULO'
    elif lados[0]**2 > (lados[1]**2 + lados[2]**2):
        tipo = 'TRIANGULO OBTUSANGULO'
    else:
        tipo = 'TRIANGULO ACUTANGULO'
    
    return tipo


def tipo_triangulo(lados):  
    tipo = None
    if lados[0] == lados[1] == lados[2]:
        tipo = 'TRIANGULO EQUILATERO'
    elif (lados[0]==lados[1]!=lados[2]) or (lados[0]==lados[2]!=lados[1]) or ((lados[1]==lados[2]!=lados[0])):
        tipo = 'TRIANGULO ISOSCELES'
    
    return tipo


entradas  = [float(num) for  num in input().split()]

entradas_ord = ordena(entradas)

if eh_triangulo(entradas_ord):
    print('NAO FORMA TRIANGULO')
else:
    print(relacao_lados(entradas_ord))
    if tipo_triangulo(entradas_ord):
        print(tipo_triangulo(entradas_ord))
  



