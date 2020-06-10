"""Recibe dos números desde el teclado. Tienes que elevar el número mayor, a la potencia del valor del número menor. Ejemplo: num_1 = 4 y num_2 = 3 -> 4 ^ 3 Imprime el resultado, indicando cuál fue el número mayor y cuál el menor. Nombre del archivo: pow_calculator.py"""

num_uno = int(input("Enter first number: "))
num_dos = int(input("Enter second number: "))

potencia = 0

if num_uno > num_dos:
    potencia = num_uno ** num_dos
    print("El num_uno",num_uno,"es mayor que el num_dos",num_dos,"y el resultado de elevar el numero mayor al numero menor es: ",potencia)
else:
    potencia = num_dos ** num_uno
    print("El num_dos",num_dos,"es mayor que el num_uno",num_uno,"y el resultado de elevar el numero mayor al numero menor es: ",potencia)

