#Ciclos: while

variable_numerica = 1

while variable_numerica <=20:
    print(str(variable_numerica))
    variable_numerica = variable_numerica+1

print("--------------")

#Si queremos entregar un fin al ciclo debemos saber como elaborarlo

input_del_usuario = input("Escribe FIN para que se termine el programa")

while input_del_usuario != "FIN":
    input_del_usuario = input("Escribe FIN para que se termine el programa: ")

#Otra forma de detener el while es usar BREAK

while True:
    print("test")
    break

print("test2")