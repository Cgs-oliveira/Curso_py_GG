#9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
#   e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.

print("#####################################")
print("############ REAL EM DOLAR ##########")
print("#####################################")

dolar = float(input("Informe a quantidade de real para conversão: R$ "))
cotacao = (float(3.45))
conversao = cotacao*dolar
print('A quantidade de real convertido em dolar é: US$ ',conversao)