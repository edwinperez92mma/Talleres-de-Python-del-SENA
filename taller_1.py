# TALLER 1 PYTHON
# AUTOR: EDWIN JOAN PEREZ BENITEZ
# FECHA: 12/06/2022

from datetime import datetime
hoy = datetime.now()
print(f"Fecha y hora actuales: {hoy}")

n1 = int(input("\nDigite el primer numero: "))
n2 = int(input("Digite el segundo numero: "))

print(f"\nEl resultado de sumar {n1} mas {n2} es: {n1 + n2}")
print(f"El resultado de restar {n1} menos {n2} es: {n1 - n2}")
print(f"El resultado de multiplicar {n1} por {n2} es: {n1 * n2}")
print(f"El resultado de dividir {n1} entre {n2} es: {n1 / n2}")

print("\nLa ejecucion del programa ha terminado")
