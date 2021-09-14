
## faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

valor = float(input("qual o valor do seu produto: R$ "))

d = valor * 0.05

desc = valor - d

print("O valor do seu produto é: R${} \nCom o desconto ficou : R$ {}".format(valor,desc))

