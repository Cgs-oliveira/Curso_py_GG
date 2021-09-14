##27) Crie um programa que leia duas notas de um aluno e calcule a sua média, 
## mostrando uma mensagem no final, de acordo com a média atingida:
##  - Média até 4.9: REPROVADO
##  - Média entre 5.0 e 6.9: RECUPERAÇÃO
##  - Média 7.0 ou superior: APROVADO

n1 = float(input("qual sua nota: "))
n2 =  float(input("qual sua nota: "))
m1= (n1 + n2)/2

print("sua media é", m1)

if m1 >= 7.0:
    print("aprovado")
elif m1 >= 5.0:
    print("recuperação")
else :
    print("reprovado")