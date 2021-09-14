#5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre
#   na tela a sua média na disciplina.


print("#####################################")
print("########## media do aluno ###########")
print("#####################################")


n1 = float(input("qual sua nota 1: "))
n2 = float(input("qual sua nota 2: "))
## divisão da nota do aluno 
##(n1 +n2) parenteses tem prioridade 
div = float(n1 + n2) / 2

print("sua média é igual: ",div)
