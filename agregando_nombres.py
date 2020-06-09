
selection = "s"
nombres = []
while selection == "s":
    nombre = input("Dame el nombre: ")
    nombres.append(nombre)
    selection = input("Deseas agregar otro nombre? ")
print(", ".join(nombres))
