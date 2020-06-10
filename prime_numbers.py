"""Un número primo es aquel que sólo es divisible entre el mismo número y el 1. Encuentra los números primeros existentes entre el 1 el 100. Posteriormente calcula el promedio de dichos números e imprímelos. Nombre del archivo: prime_numbers.py"""

import math

contador = 0
suma = 0

for num in range(2,101):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
        print (num)
        suma += num
        contador += 1
    
avg = suma / contador
print("El promedio de los {} numeros es igual a {}.".format(contador, avg))