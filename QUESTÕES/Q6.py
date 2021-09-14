#6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu
#   sucessor.


print("#######################################")
print("####### antecessor / sucessor #########")
print("#######################################")

n = int(input("digite um numero: "))
a = n - 1
s = n + 1
## O método format() serve para criar uma string que contem campos entre chaves a serem substituídos pelos argumentos de format.
## Programa para testar a função format()

## s = 'Adoro Python'

## alinha a direita com 20 espaços em branco
## print("{0:>20}".format(s))

## alinha a direita com 20 símbolos #
##print("{0:#>20}".format(s))

## alinha ao centro usando 10 espaços em branco a esquerda e 10 a direita
## print("{0:^20}".format(s))

## imprime só as primeiras cinco letras
## print("{0:.5}".format(s))


print ("analisando... {},seu sucessor é {}, seu antecessor é {}".format(n, s, a))
print ("num digitado ",n, "sucessor ",s, "antecessor", a)

