
## faça um programa que leia a largura e a altura de uma parede e metros, calcule a area  e a quantidade de tinta nescessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m².


lag = float(input("Largura da parede: "))

alt = float(input("Altura da parede: "))

## area da parede

area = lag * alt

## tinta

tinta = area / 2

print("A quantidade de Litros para essa parede: L",tinta)
