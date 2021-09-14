##16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
##      fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
##      já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
##      quantos dias de vida um fumante perderá e exiba o total em dias.


quant_c = int(input("quantos cigarros voce fuma por dia? "))

quant_a = int(input("quantos anos você fuma? "))

# a cada 1 cigarro ele perde 10min
# a cada 6 cigarros ele perde 60min
# para sabermos a perca percentual por hora temos que dividir 10/60
# chegamos em 0,16 (relção de perca caso ele fume apenas 1 cigarro em 60 min)

# tempo perdido/dia = quantidade de cigarros * 3,84 (24) 
# explicação da formula para min perdidos por dia

temp_ano = (quant_a * 365) * quant_c * 10

# um dia tem 24 X 60 min = 1440

temp_dia = temp_ano / 1440



print("Você fuma {} cigarros por dia e a {} anos vc faz uso diario, Você tem {:.2f} DIAS a menos de vida, ".format(quant_c, quant_a,temp_dia))

