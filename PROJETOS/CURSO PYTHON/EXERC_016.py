
##importação

## crie um programa quie leia um numero real e mostre apenas sua parte inteira na tela 
## EX: 6.435 = 6

import math

num = float(input("digite um numero: "))
#importando o modulo.
arr = math.floor(num)

print("seu numero arredondado é:",arr)
