# TALLER 4 PYTHON
# AUTOR: EDWIN JOAN PEREZ BENITEZ
# FECHA: 16/06/2022

#---------------Fecha y hora---------------#
from datetime import datetime
hoy = datetime.now()
print(f"Fecha y hora actuales: {hoy}")

#---------------1ra parte---------------#
print("\nEjercicio de las clases de triangulos\n")

a = int(input("Digite el valor de a: "))
b = int(input("Digite el valor de b: "))
c = int(input("Digite el valor de c: "))

def tipos_triangulos(a, b, c):
    if a==b and a==c and b==c:
        return "El triangulo es equilatero\n"
    elif a==b or b==c or a==c:
        return "El triangulo es isoceles\n"
    else:
        return "El triangulo es escaleno\n"

print(tipos_triangulos(a, b, c))

#---------------2da parte---------------#
print("Animales\n")

def tipos_animales():

    animal = input("Digite el nombre de un animal: ")
    animal = animal.upper()

    if animal == "PERRO":
        print(f"Este animal es el mejor amigo del hombre: {animal}\n")
    elif animal == "GATO":
        print(f"Este animal persigue a los ratones: {animal}\n")
    elif animal == "OSO":
        print(f"Este animal vive en el polo norte: {animal}\n")
    else:
        print(f"No es PERRO, no es GATO, ni es OSO... es: {animal}\n")

tipos_animales()

print("La ejecucion del programa ha terminado")
