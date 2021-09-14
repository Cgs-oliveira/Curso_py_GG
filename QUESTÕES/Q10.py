##10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e
##    mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
##    sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

# a = altura
a = float(input("qual a altura da parede: "))
# l = largura
l = float(input("qual a largura da parede: "))
# ap = area da parede
ap = a * l

print ("area da parede é ", ap)

# lt = litro de tinta
lt = ap / 2

print ("são nescessarios ", lt, "l de tinta para pintar essa parede.")




