## 11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
## segundo grau e mostre o valor de Delta.


a = int(input("qual o valor de A na equação: "))
b = int(input("qual o valor de B na equação: "))
c = int(input("qual o valor de C na equação: "))

## formula do delta Δ = b2 – 4ac

delta = (b**2) - 4 * (a) * (c)

print ("o valor de delta 'Δ' é: ", delta)

