
## FAÇA UM PORGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIANGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.


## sem importação

'''co = float(input("qual o valor do cateto oposto? "))
ca = float(input("qual o valor do cateto adjacente? "))
## multiplicar qualquer numero por 0.5 ou 1/2 é a mesma coisa que chamar sua raiz
hi = (co**2 + ca**2)**(0.5)

print("o valor da hipotenusa é: {:.2f}".format(hi))'''

## com impotação

import math

co = float(input("qual o valor do cateto oposto? "))
ca = float(input("qual o valor do cateto adjacente? "))
hi = math.hypot(co,ca)

print("o valor da hipotenusa é: {:.2f}".format(hi))

