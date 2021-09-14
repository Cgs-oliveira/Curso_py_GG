##
##25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta.
##      Analise seus comprimentos e diga se é possível formar um triângulo com essas
##      retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento
##      de cada lado deve ser menor que a soma dos outros dois.


## l1 < l2 +l3 ou l2 < l1 +l2 ou l3 < l1 + l2


l1 = float(input("primeiro segmento : "))
l2 = float(input("segundo segmento : "))
l3 = float(input("terceiro segmento : "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("forma um triangulo")
else:
    print("não forma um triangulo")
