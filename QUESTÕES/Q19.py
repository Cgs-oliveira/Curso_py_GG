

## 19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
## média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
## não um bom aproveitamento (se ficou acima da média 7.0).


nota1 = float(input("digite sua nota: "))
nota2 = float(input("digite sua nota: "))

media = (nota1 + nota2)/2
print("sua media é ",media)

if media >= 7:
    print("aprovado, meus parabéns ")
else:
    print("você está reporvado")



