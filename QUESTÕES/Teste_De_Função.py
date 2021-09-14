## é pra analisar uma partida entre dois times, e falar a diferença de gols e status, o status seria (partida normal, goleada e empate)

print("em caso de empate entre os times não faz diferença a sequência \n")

time1 = int(input( "quantos gols o time vencedor fez : "))

time2 = int(input( "quantos gols o time perdedor fez : "))

result = (time1 - time2)


if result >= 4:
    print("goleada!!!")
elif result > 0  and result <= 3:
    print("jogo normal. ")
else:
    print("empate")




