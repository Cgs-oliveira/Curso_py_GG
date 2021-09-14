
## Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

## Onde C é a temperatura em graus Celsius e F, a temperatura em Fahrenheit. Ao simplificarmos a fórmula, temos: 
## F = C x 1,8 + 32.

temp_c = float(input("temperatura Celsisus °C: "))

F = temp_c * 1.8 + 32

print("A temperatura em Fahrenheit °F: ",F)
