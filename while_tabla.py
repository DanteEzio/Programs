selection = "si"

while selection == "si":
    number = int(input("Dame el numero para la tabla de multiplicar: "))
    counter = 1
    while counter < 26:
        print(f"{number} x {counter} = {number * counter}")

        counter += 2

    selection = input("Deseas calcular otra tabla de multiplicar? (si/no)")
print("Adios!")

