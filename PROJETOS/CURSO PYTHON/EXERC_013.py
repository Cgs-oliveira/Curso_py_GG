
## faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.

sal = float(input("quanto é seu salario atual? "))

aumento = sal * 0.15

alt_sal = aumento + sal

print("Seu salario com o aumento de 15% R$:{}".format(alt_sal))
