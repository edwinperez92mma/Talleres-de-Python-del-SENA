# TALLER 3 PYTHON
# AUTOR: EDWIN JOAN PEREZ BENITEZ
# FECHA: 14/06/2022

#---------------Fecha y hora---------------#
from datetime import datetime
hoy = datetime.now()
print(f"Fecha y hora actuales: {hoy}")

#---------------1ra parte---------------#
a = int(input("\nDigite el valor de a: "))
b = int(input("Digite el valor de b: "))

if a > b:
    print(f"A({a}) es mayor que B({b})\n")
elif a == b:
    print(f"A({a}) es igual a B({b})\n")
else:
    print(f"A({a}) es menor que B({b})\n")

#---------------2da parte---------------#
opcion_1 = int(input("Presione 1 si estudia Requerimientos\nPresione 2 si estudia otra área: "))
opcion_2 = int(input("\nPresione 1 si estudia Algoritmos\nPresione 2 si estudia otra área: "))

curso_1 = ""
curso_2 = ""

if opcion_1 == 1:
    curso_1 = "Requerimientos"
else:
    curso_1 = "Otra no disponible"


if opcion_2 == 1:
    curso_2 = "Algoritmos"
else:
    curso_2 = "Otra no disponible"
    
print(f"Nombre del primer curso: {curso_1}")
print(f"Nombre del segundo curso: {curso_2}\n")

if curso_1 == "Requerimientos" and curso_2 == "Algoritmos":
    print("Usted estudia Programacion de Software\n")
elif curso_1 == "Requerimientos" and curso_2 != "Algoritmos":
    print("Usted solo estudia Requerimientos\n")
elif curso_1 != "Requerimientos" and curso_2 == "Algoritmos":
    print("Usted solo estudia Algoritmos\n")
else:
    print("Usted estudia un programa distinto a Programacion de Software\n")

cadena = "Final del Análisis del Programa de formación del sena"
print(cadena.center(70, "*"))

#---------------3ra parte---------------#

frase = input("\nDigite una oración: ")

print(f"La frase en mayuscula es: {frase.upper()}")

longitud = len(frase)

print(f"La longitud de la frase es: {longitud} caracteres")

if longitud > 10:
    print(f"La frase '{frase}' contiene mas de 10 caracteres")
else:
    print(f"La frase '{frase}' contiene menos de 11 caracteres")

print("\nLa ejecución del programa ha terminado")
    
