##  17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
##      80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
##      o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

velocidade = int(input("qual a velocidade do seu carro em KM\h: "))

if velocidade >= 81:
    # velocidade - 80  pega o resultado e aplica na multa * 5 
    velc1 = velocidade - 80
    multa = velc1 * 5
    print("você foi multado em R$:",multa )
else:
    print("você está na velocidade certa")




