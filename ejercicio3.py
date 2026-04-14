#Se dará un bono de navidad a los trabajadores que será equivalente a 25000 + 25% de su sueldo

bono= 25000
empleado = input("Ingrese su nombre:")
sueldo = int(input("Ingrese el monto de su sueldo mensual:"))
bono_navidad = sueldo*0.25+bono

bonos_calculados = 0
bonos_calculados +=1

print("Nombre:", empleado)
print("Bono navidad:", bono_navidad)
print("Bonos calculados", bonos_calculados)