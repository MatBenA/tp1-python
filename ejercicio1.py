nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
fechaNacimiento = input("Ingrese su fecha de nacimiento: ")
matricula = int(input("Ingrese monto de matricula: "))

print()
print("=======================================================")
print("======== Universidad de Python - Inscripciones ========")
print("=======================================================")
print()

arancelPythonI = 12000
pythonIMensual = arancelPythonI / 4
pythonConDescuento = pythonIMensual * 0.85

print("DATOS DE INGRESO: ")
print("Nombre completo: ", nombre)
print("Fecha de nacimiento y edad: ", fechaNacimiento, " (", edad, ")")
print("Posee titulo?: ", True)
print("Matricula: ", matricula)
print("Cuota mensual: ", matricula + 1000)
print("Arancel mensual materia 'Python I': ", pythonIMensual)
print("Arancel mensual materia 'Python I' con descuento: ", pythonConDescuento)