##30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo 
## de triângulo será formado: 
## - EQUILÁTERO: todos os lados iguais
## - ISÓSCELES: dois lados iguais
## - ESCALENO: todos os lados diferentes

## matematicamente resumido é isso:
## l1 < l2 + l3  ou l2 < l1 + l3 ou l3 < l2 + l1

l1 = int(input("primeiro segmento: "))
l2 = int(input("segundo segmento: "))
l3 = int(input("terceiro segmento: "))



if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 +l2:
    print("forma um triângulo !!!!")
    if l1 == l2 == l3:
        print("EQUILÁTERO")
    elif l1 != l2 != l3:
        print("ESCALENO")
    else:
        print("ISÓSCELES") 
    
else:
    print("não forma um triângulo !!!!")

