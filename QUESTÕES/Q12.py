## 12) Crie um programa que leia o preço de um produto, calcule e mostre o seu
##     PREÇO PROMOCIONAL, com 5% de desconto.

valor = float(input("Valor do produto: "))
v_porcent = valor * 0.05

valor_desc = valor - v_porcent

print ("produto com o disconto de 5% é: ",valor_desc)

