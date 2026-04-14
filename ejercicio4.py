#Se entregará un bono de fin de año de 45000 a cada empleado, y a esto se le sumará
#un beneficio de 10000 por cada año que lleve en la empresa: bono por años de servicio, solo
#para empleados que llevan 5 o mas años en la empresa

bono_base = 45000
bono_por_años = 10000


def bono_por_antiguedad(años_de_servicio):
    if años_de_servicio <5:
        return 0
    else:
        años_de_servicio*bono_por_años

empleado = input("Ingrese su nombre:")
años_de_servicio = int(input("Ingrese sus años de servicio en la empresa:"))
bono_por_años = bono_por_antiguedad(años_de_servicio)
bono_total = bono_base+bono_por_años


print("Nombre:", empleado)
print("Bono_base:", bono_base)
print("Bono por años de servicio", bono_por_años)
print("Bono total", bono_total)
