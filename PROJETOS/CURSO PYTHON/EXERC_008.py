
## ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E CONVERTA EM CENTIMETROS E MILIMETROS

metro = float(input("digite um numero em M para ser convertido em CM e MM: "))

## conversão para MM

convet = metro * 1000

## conversão para CM

convet2 = metro * 100

print("{0} convertido em MM é: {1}mm, e convertido em CM é: {2}cm".format(metro,convet,convet2))

