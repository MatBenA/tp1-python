# Punto A
print("===========================================================")
dia = int(input("Ingrese el numero del día: 1 (lunes) a 6 (sábado): "))
aula = "A-315"
if (dia % 2 == 0): aula = "A-300"
print("Aula: ", aula)
print()

# Punto B
print("===========================================================")
turno = input("Ingrese el turno: Mañana, Tarde o Noche: ")
cantidadMaterias = int(input("Ingrese la cantidad de materias: "))

cuota = 10000
if(turno == "Tarde" and cantidadMaterias > 3): cuota = cuota * 0.75
else: cuota = cuota * 0.95
print("El valor de las cuota es: ", cuota)


# Punto C
vehiculo = input("Ingrese el vehiculo en el que ingresa: Auto, Moto o Bicicleta: ")
costoEstacionamiento = 300
if (vehiculo == "Bicicleta"): costoEstacionamiento = 50
print("El costo de estacionamiento para ", vehiculo, " es: ", costoEstacionamiento)