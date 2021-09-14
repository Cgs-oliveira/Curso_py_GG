##15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o
##    salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
##    por hora trabalhada.

dia_t = float(200)
hora_t = float(25) 

dt = int(input("digite quantos dias você trabalhou esse mês: "))
print("\n")

ht = int(input("quanta horas você trabalho: "))
print("\n")

pg_mes = dt * dia_t
pg_hora = ht * hora_t

sal_mes = pg_mes + pg_hora

print("você ira receber pelos dias trabalhados: R$ ", sal_mes)




