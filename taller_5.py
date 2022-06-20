# TALLER 5 PYTHON
# AUTOR: EDWIN JOAN PEREZ BENITEZ
# FECHA: 17/06/2022

#---------------Fecha y hora---------------#
from datetime import datetime
hoy = datetime.now()
print(f"Fecha y hora actuales: {hoy}")

#---------------1ra parte---------------#
print("\nTaller 5 - Ciclos iterativos con la sentencia 'for'\n\n1ra parte\n")

num_1 = int(input("Digite el primer numero entero: "))
num_2 = int(input("Digite el segundo numero entero: "))

print("\nCiclo para el primer numero\n")

def primer_ciclo(num_1):
    for i in range(num_1):
        print(f"Viendo el valor: {i}")
    print("Fin del primer ciclo\n")

primer_ciclo(num_1)

print("Ciclo desde el primer número hasta el segundo numero\n")

def segundo_ciclo(num_1, num_2):
    for i in range(num_1, num_2):
        print(i, end=" ")
    print("\nFin del segundo ciclo\n")

segundo_ciclo(num_1, num_2)

print("Ciclo desde el primer número hasta el segundo numero con incrementos de 2\n")

def tercer_ciclo(num_1, num_2):
    lista = []
    for i in range(num_1, num_2, 2):
        lista.append(i)
        print(f"Insertando valores en la lista: {lista}")
    print("Fin del tercer ciclo\n")

tercer_ciclo(num_1, num_2)

#---------------2da parte---------------#

print("2da parte\n")

empresa = input("Digite el nombre de una empresa: ")
empresa = empresa.title()

lista = []
lista_str = None

def ciclo_empresa(nombre):
    for i in empresa:
        lista.append(i)
        lista_str = "".join(lista)
    print(f"La empresa '{lista_str}' es genial")
    print("Fin del ciclo\n")

ciclo_empresa(empresa)

print("La ejecución del programa ha terminado")