

# uso do for

##for i in range(10):
##    print(i)

## uso do while

## soma = 0
## while soma < 200:
##     print(soma)
##     soma = soma + 1


import random

## nome dos alunos sorteados



al1 = ("pedra")
al2 = ("papel")
al3 = ("tesoura")

## lista de alunos 

lista = [al1, al2, al3,]

## na duvida verifica o choice

escolhido = random.choice(lista)

print("o computador escolheu: {}".format(escolhido))