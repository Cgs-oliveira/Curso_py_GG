## 14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
##     um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
##     quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
##     sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

dias = int(input("quantos dias você ficou com o nosso carro? \n"))
cobr_dia = dias * 90

valor_km = int(input("quantos KM você percorreu com nosso carro? \n"))
print("\n")
cobr_km = valor_km * 0.20

valor_pg = cobr_dia + cobr_km

print ("agradecemos a sua preferência. em caso de reclamação ou elogio entre em contato com nossa central de atendimento \n")
print ("caso tenha esquecido algo dentro do carro venha até nosso achados e perdidos \n")
print ("após a verificação do carro va ate o caixa e pague o valor de: R$ ")
print ("R$: ",valor_pg)

print("\n")
print("\n")

print("-- _____DD_        ")
print("-/__\\____\____    ")
print("/…._.|-….|……._.o\  ")
print("=’(@)--------(@)-´ ")
