paises = ["MX", "US", "UK", "MX", "MX", "US", "UK", "FR", "CH", "CH"]
print(paises)

#Agrega el elemento que solicitemos a la lista
paises.append("JP")
print(paises)

#Este metodo nos indica el numero de veces que se encuentra nuestro argumento
print("El elemento MX se encuentra: ",paises.count("MX"), "veces")


print("El elemento UK se encuentra por primera vez en el indice: ", paises.index("UK"))

paises_copy = paises.copy()
print(paises_copy)

paises_copy.extend(["COL","ARG","BR"])
print(paises_copy)

paises_copy.remove("CH")
print("La lista sin la palabra CH es: ", paises.copy)