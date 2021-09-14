
## O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATROS ALUNOS E MOSTRE A ORDEM SORTEADA.

import random
n1 = input("nome: ")
n2 = input("nome: ")
n3 = input("nome: ")
n4 = input("nome: ")

lista = [n1,n2,n3,n4]
## embaralhar 
random.shuffle(lista)

print("o aluno escolhido é ",lista)