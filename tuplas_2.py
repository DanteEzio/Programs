names = input("Dame los nombres, separados por una coma: ")
names_list = names.split(",")
print(names_list)
names_tuple = tuple(names_list)
print(names_tuple)
print(f"La cantidad de elementos en la tupla es: {len(names_tuple)}")
print(f"El valor maximo de en la tupla es: {max(names_tuple)}")
print(f"El valor minimo en la tupla es: {min(names_tuple)}")