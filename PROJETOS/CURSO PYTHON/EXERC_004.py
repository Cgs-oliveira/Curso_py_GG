## dessecando uma varialvel 
## faça um programa de voce digite algo no teclado, e o programa dê o maximo de informação sobre o que foi digitado
## 

a = (input("digite algo para analise: "))

print("são só espaços? ",a.isspace())
print("são só números? ",a.isnumeric())
print("são números e letras? ",a.isalnum())
print("são apenas letras ? ",a.isalpha())
print("são caracteres ASCII? ",a.isascii())
print("são maiusculas ? ",a.isupper())
print("são miusculas ? ",a.islower())
print("tem maiusculas e minusculas ?",a.istitle())
