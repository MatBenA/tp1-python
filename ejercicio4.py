# Punto A
print("Día      Aula")

for i in range(1, 6):
    aula = "A - 315"
    if (i % 2 == 0): aula = "A - 300"
    print(i, "      ", aula)

# Punto B
print()
print("================ Carga de edades ================")

edad = int(input("Ingrese una edad igual o mayor a 18: "))
cantidadErrores = 0

while (edad < 18):
    cantidadErrores += 1
    edad = int(input("Error! Ingrese una edad igual o mayor a 18: "))

print("La edad ingresada es: ", edad)
print("Se ha ingresado la edad erroneamente ", cantidadErrores, " veces")

# Punto C
print()
print("================ Promedio de notas ================")
total = 0
for i in range(0, 5):
    nota = int(input("Ingrese la nota: "))
    total = total + nota

print("El promedio de notas es: ", total / 5)

# Punto D
print()
print("================ Costo del comedor ================")
costo = 0
for i in range(1,7):
    costo += 1250
    print(i, "       $ ", costo)