"""Programa para identificar si
un numero dado es par o impar"""

print("--------------------------------------")
print("------Numero Par o Impar-------------")
print("--------------------------------------")

#input
X = int(input("digite el valor de X: "))

#processing

Z = X % 2

if Z == 1:
    msj = "El numero dado es impar"

else:
    msj = "El numero dado es par"

#output

print(msj)