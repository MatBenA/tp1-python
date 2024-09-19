primerNota = int(input("Ingrese la nota del primer parcial: "))
segundaNota = int(input("Ingrese la nota del segundo parcial: "))
promedio = (primerNota + segundaNota) / 2

print()
print("El promedio de las notas es: ", promedio)

if( segundaNota >= 7 ):
    print("Aprobó el segundo parcial")
else:
    print("Desaprobó el segundo parcial")


progreso = "Empeoró su desempeño"

if ( segundaNota > primerNota): 
    progreso = "Mejoró su desempeño"
elif ( segundaNota == primerNota ):
    progreso = "Mantuvo la nota"

print("Progreso del 1er al 2do parcial: ", progreso)

if ( promedio >= 7 ): 
    print("Promociono la materia")
else:
    print("No promocionó la materia")