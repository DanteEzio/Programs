"""Un número primo es aquel que sólo es divisible entre el mismo número y el 1. Encuentra los números primeros existentes entre el 1 el 100. Posteriormente calcula el promedio de dichos números e imprímelos. Nombre del archivo: prime_numbers.py"""

for num in range(1,101):
    for i in range(2,num):
        if(num%i==0):
            break
        else:
            print(num)
            break
