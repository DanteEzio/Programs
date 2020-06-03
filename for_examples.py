#Imprime los 300 primeros numeros pares
for i in range(2,301,2):
    print(i)

#Imprime la tabla del 15. Muestra el resultado de los primeros 20 numeros
numero = int(input("Enter number: "))
for i in range(1,21):
    resultado = i*numero
    print(("%d X %d = %d")%(numero,i,resultado))

#Calcula la suma de los numeros impares ubicados entre el 50 y el 100
suma_impares = 0

for i in range(50,100):
    if i % 2 == 1:
        suma_impares += i
        print("La suma de los numeros impares ubicados entre el 50 y el 100 es: ",suma_impares)

#Calcula la suma de los numeros pares ubicados entre el 10 y el 100
suma_pares = 0

for i in range(10,101):
    if i % 2 == 0:
        suma_pares += i
        print("La suma de los numeros pares ubicados entre el 10 y el 100 es: ",suma_pares)


