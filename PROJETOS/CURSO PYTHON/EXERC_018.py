
## FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO COSSENO E TANGENTE DESSE ANGULO. 

import math

angulo = float(input("angulo: "))
seno = math.sin(math.radians(angulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(angulo,seno))

cos = math.cos(math.radians(angulo))
print("O angulo de {} tem o COS de {:.2f}".format(angulo,cos))

tan = math.tan(math.radians(angulo))
print("O angulo de {} tem TAN de {:.2f}".format(angulo,tan))


