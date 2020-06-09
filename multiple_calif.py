

selection = "si"
nombre = input("Ingresa tu nombre: ")
califs = []
while selection == "s":
    calif = float(input("Dame la calificacion: "))
    califs.append(calif)
    selection = input("Deseas agregar otra calificacion?: (s/n): ")
acum = 0
for calif in califs:
    acum += calif
mean = acum / len(califs)
print(f"El promedio del alumno {nombre} es: {mean}")


