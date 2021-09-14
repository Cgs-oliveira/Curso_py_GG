

#26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
#na tela uma das mensagens abaixo:
# - O primeiro valor é o maior
# - O segundo valor é o maior
# - Não existe valor maior, os dois são iguais

n1 = float(input("digite um número: "))
n2 = float(input("digite outro numero: "))

if n1 > n2:
    print("o primeiro é maior: ", n1)
elif n1 < n2:
    print("o segundo é maior: ", n2)
else:
    print("Não existe valor maior, os dois são iguais")
