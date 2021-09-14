#7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a
#   sua terça parte.

n = float(input("numero para analise: "))
d = n * 2
t = n / 3

# O ".format" com o :.2f é para limitar o numero "quebrado" a apenas 2 numeros depois do ponto.

print("analise..{}, dobro {:.2f}, terça parte {:.2f}".format(n, d, t))



