##29) Desenvolva um programa que leia o nome de um funcionário, seu salário, 
##quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de 
##acordo com a tabela a seguir:
## - Até 3 anos de empresa: aumento de 3%
## - entre 3 e 10 anos: aumento de 12.5%
## - 10 anos ou mais: aumento de 20%


print ("tabela de aumento 3 anos de empresa 3%, 3-10 anos de empresa 12,5%, 10+ de empresa 20%")


func = input("qual seu nome : ")
anos_t = int(input("quantos anos voce tem na empresa: "))
sal = float(input("quanto é o seu salario bruto: "))

if anos_t == 3:
    aumt1 = (sal * 0.03) + sal
    print ("{}, seu salario agora é: R${}".format(func,aumt1))
elif anos_t <= 10:
    aumt2 = (sal * 0.125) + sal
    print ("{}, seu salario agora é: R${}".format(func,aumt2))
else :
    aumt3 = (sal * 0.20) + sal
    print("{}, seu salario agora é P: R${}".format(func,aumt3))


