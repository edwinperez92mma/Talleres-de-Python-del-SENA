import random

# TALLER 6 PYTHON
# AUTOR: EDWIN JOAN PEREZ BENITEZ
# FECHA: 18/06/2022

#---------------Fecha y hora---------------#
from datetime import datetime
hoy = datetime.now()
print(f"Fecha y hora actuales: {hoy}")

#---------------1ra parte---------------#
print("Taller 6 - Ciclos iterativos con la sentencia while\n")

print("---------------Primera parte---------------\n")

num_1 = int(input("Digite un numero: "))

print("\n***Ciclo controlado por contador***")

i = 1

def ciclo_1(i):
    while i <= num_1:
        print(i)
        i += 1

ciclo_1(i)

print("Fin del primer ciclo\n")

#---------------2da parte---------------#
print("---------------Segunda parte---------------\n")

print("***Ciclo controlado por evento***\n")

print("Juego: adivina el número")

j = 0

def adivina(j):

    numero_1 = random.randint(1, 10)
    numero_2 = int(input("Digite un numero de 1 a 10: "))

    while numero_2 != numero_1:
        
        if numero_2 > numero_1:
            j += 1
            print("Numero muy alto")
            numero_2 = int(input("Digite un numero de 1 a 100: "))

        if numero_2 < numero_1:
            j += 1
            print("Numero muy bajo")
            numero_2 = int(input("Digite un numero de 1 a 100: "))

    if numero_2 == numero_1:
        j += 1
        print("¡Lo lograste!")
        print(f"Te tomó {j} intentos")

adivina(j)

print("Fin del primer ciclo\n")

#---------------3ra parte---------------#
print("---------------3ra parte---------------\n")

print("***Ciclo abortado con la sentencia break***\n")

amistad = input("Digite el nombre de una amistad: ")
amistad = amistad.upper()

def analizar_amistad(amistad):
    for k in amistad:
        print(k)
        if k == "A":
            print(f"Analizando la letra '{k}'...")
            print("\nEncontramos una vocal 'A' en el nombre de tu amistad")
            print("¡Este programa es incapaz de procesar las 'A'!\n¡Error! ¡Error! ¡Error!\n")
            break
    print("Ciclo terminado")

analizar_amistad(amistad)

print("La ejecución del programa ha terminado")
