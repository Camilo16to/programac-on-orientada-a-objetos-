from zipfile import ZIP_BZIP2
from persona import Persona
from zombi import Zombi

import os

os.system ("cls")

print()
print(" La ciudad se ha llenado de zombis.")
print ("Estás en la calle 1 y has de llegar")
print ("a la calle 40 para poder salvarte.")
print()
print("Los zombis avanzan 1, 2 ó 3 calles.")
print ("tu puedes avanzar 1, 2 ó 3 calles.")
print()
nombre = input ("¿Estas preparado? Cuál es tu nombre: ").capitalize()

jugador = Persona (nombre)

horda = []
for i in range (20):
    z= Zombi()
    horda.append (z)

while True:

    os.system ("cls")

    print (jugador.situacion())

    calles = []
    for zombi in horda:
        print (zombi.calle)
    calles.sort()
    print ("hay zombis en las calles:")
    for elemento in calles:
        print (elemento, end=" ")
    print()

    