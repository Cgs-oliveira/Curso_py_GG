## 20) Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou
##      ÍMPAR.

n = int(input("digite um numero: "))

## % = resto, então se resto = 0 é par

real = n % 2

if n == 0:
    print("o numero é par") 
else:
    print("impar")