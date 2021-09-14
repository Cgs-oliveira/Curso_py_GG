##8) Desenvolva um programa que leia uma distância em metros e mostre os valores
## relativos em outras medidas.
## Ex:
## Digite uma distância em metros: 185.72
## A distância de 85.7m corresponde a:
## 0.18572Km
## 1.8572Hm
## 18.572Dam
## 1857.2dm
## 18572.0cm
## 185720.0mm



medida = float(input("digite quantos metros para conversão:"))

## De metros até km divide e sobe um zero na divisão
km = medida / 1000
hm = medida / 100
dam = medida / 10

## De metros até milimetros multiplica subindo um zero na multiplicação
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print ("medidas M: {}, km: {}, hm: {}, dam: {}, dm: {}, cm: {}, mm: {}".format(medida, km, hm, dam, dm, cm, mm))
