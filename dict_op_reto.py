diccionario = {}
selection = "s"
while selection == "s":
    pais = input("Ingresa el pais: ")
    personas_viviendo = int(input("Ingresa el numero de personas viviendo en este pais: "))
    diccionario[pais] = personas_viviendo
    selection = input("Deseas agregar otro pais? ")

for clave, valor in diccionario.items():
    print(f'Pais: {clave}, Cantidad de habitantes: {valor}')

country_to_see = input("Dame el pais que deseas ver: ")
print(f'La cantidad de habitantes en {country_to_see} es: {diccionario[country_to_see]} millones de personas')







