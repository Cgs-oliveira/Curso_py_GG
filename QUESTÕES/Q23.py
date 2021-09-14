## 23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
## para todos, mas especialmente para mulheres. Faça um programa que leia nome,
## sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo
## que:
## - Homens ganham 5% de desconto
## - Mulheres ganham 13% de desconto

valor = float(input("valor da mercadoria comprada: "))
opcao = 0
while opcao != 3:
    print ('''qual seu sexo?
    [1] para homem
    [2] para mulher
    [3] para sair''')

    #criando condições
    if opcao == 1:
        desc_h = valor * 0.05
        valor_dh = desc_h + valor
        print("sua peça com desconto é: R$", valor_dh)
    elif opcao == 2:
        desc_f = valor * 0,15
        valor_df = desc_f + valor
        print("sua peça com o desconto é: R$", valor_df)
    opcao = int(input("escolha uma opção"))
print("Fim do programa.")

