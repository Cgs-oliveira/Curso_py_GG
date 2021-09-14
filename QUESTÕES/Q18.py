##18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
## dela e depois mostre se ela pode ou não votar.


idade = int(input("Qual ano você nasceu? "))

vot = 2021 - idade

print ("você tem", vot, "anos")

if vot >= 16:
    print("você ja pode votar ")
else:
    print("você não tem idade para votar ainda, mete o pé..")

