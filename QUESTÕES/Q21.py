## 21) Faça um algoritmo que leia um determinado ano e mostre se ele é ou não
## BISSEXTO.

ano = (int(input("digite os dois ultimos numeros do ano, EX: 2010 = 10 ")))

ano_b = ano % 4

if ano_b == 0:
    print("é ano bissexto")
else:
    print("não é ano bissexto")