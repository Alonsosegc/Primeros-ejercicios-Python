#Ademas de while, se puede usar el FOR

variable_numerica = 1

while variable_numerica <= 20:
    print(str(variable_numerica))
    variable_numerica = variable_numerica + 1

#Ocupando el FOR se genera una eficiencia en el comando ejecutan lo mismo
#Cuando utilizamos el IN RANGE nos indicará que el recorrido irá desde
#El límite inferior (1) hasta el límite superior -1, osea (21-1)= 20.

for variable_numerica in range(1,21):
    print(str(variable_numerica))