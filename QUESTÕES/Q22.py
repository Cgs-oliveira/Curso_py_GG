##22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
## situação em relação ao alistamento militar.
## - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o
## alistamento.
## - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do
## alistamento.

q_ano = int(input("qual ano você nasceu? "))

alist = 2021 - q_ano

if alist <= 18:
    print("você ainda não tem idade para o alistamento obrigatorio militar, você tem:",alist)
else:
    print(" você já pode se alistar, você tem: ",alist," vá ate uma junta de serviço militar ou entre no site: www.alistamentoonline.org.br")


