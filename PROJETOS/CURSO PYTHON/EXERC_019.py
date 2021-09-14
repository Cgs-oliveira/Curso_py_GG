
## UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADOR FAÇA UM PROGRAMA QUE AJUDE ELE LENDO O NOME DELES E ESCREVA O NOME DO ESCOLHIDO

import random

## nome dos alunos sorteados



al1 = input("nome do aluno: ")
al2 = input("nome do aluno: ")
al3 = input("nome do aluno: ")
al4 = input("nome do aluno: ")

## lista de alunos 

lista = [al1, al2, al3, al4]

## na duvida verifica o choice

escolhido = random.choice(lista)

print("o aluno escolhido foi: {}".format(escolhido))

