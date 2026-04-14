#Mediante un número al azar se dispondrá a cada persona a un grupo determinado

import random
nombre = input("Ingrese su nombre:")
numero_grupo = random.randint(1,3)

if numero_grupo==1:
    print(nombre + " Fuiste asignado al Grupo Alerce")
elif numero_grupo==2:
    print(nombre + " Fuiste asignado al Grupo Roble")
else:
    print(nombre + " Fuiste asignado al Grupo Cerezo")



