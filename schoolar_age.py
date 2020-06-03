nombre = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 6:
    print("Kinder")
elif age >= 6 and age < 12:
    print("Primaria")
elif age >= 12 and age < 15:
    print("Secundaria")
elif age >= 15 and age < 18:
    print("Bachillerato")
elif age >= 18 and age < 23:
    print("Universidad")
else:
    print("Profesionista")