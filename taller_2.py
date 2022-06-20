# TALLER 2 PYTHON
# AUTOR: EDWIN JOAN PEREZ BENITEZ
# FECHA: 13/06/2022

#Fecha y hora
from datetime import datetime
hoy = datetime.now()
print(f"Fecha y hora actuales: {hoy}")

#1ra parte
a = int(input("\nDigite el primer numero: "))
b = int(input("Digite el segundo numero: "))
c = int(input("Digite el tercer numero: "))

x = [a, b, c]

print(f"\nEl valor maximo es: {max(x)}")
print(f"El valor minimo es: {min(x)}")
print(f"La suma de los 3 numeros enteros es: {sum(x)}\n")

#2da parte
z = float(input("Digite un numero con decimales: "))
redondo = round(z)
print(f"El valor de {z} redondeado es: {redondo}\n")

#3ra parte
frase = input("Digite una oracion: ")
print(f"La frase en mayusculas es: {frase.upper()}")
print(f"La frase en minusculas es: {frase.lower()}")
print(f"La frase en mayuscula inicial es: {frase.capitalize()}")
print(f"La frase con la primera letra de las palabras en mayuscula es: {frase.title()}")
print(f"La longitud de la frase es de {len(frase)} caracteres incluyendo espacios en blanco")

print("\nLa ejecucion del programa ha terminado")
