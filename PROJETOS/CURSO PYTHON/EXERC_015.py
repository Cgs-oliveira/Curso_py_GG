
## Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


dia = float(input("dias com automovél: "))

alugdia = 60 * dia

kmr = float(input("quantos KM você rodou: "))

km = 0.15 * kmr

alug1 = alugdia + km

print("O valor do alguel dia e KM  R$",alug1)

