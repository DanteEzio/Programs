nombre = input("Enter your name: ")
age = int(input("Enter your age: "))
prom = float(input("Enter your average: "))

if age < 6 and prom >= 10:
    print("Kinder, promedio aceptable")
elif age < 6 and prom < 10:
    print("Kinder, promedio triste")
elif age >= 6 and age < 12 and prom >= 9.5:
    print("Primaria, promedio aceptable")
elif age >= 6 and age < 12 and prom < 9.5:
    print("Primaria, promedio triste")
elif age >= 12 and age < 15 and prom >= 9:
    print("Secundaria, promedio aceptable")
elif age >= 6 and age < 12 and prom < 9:
    print("Secundaria, promedio triste")
elif age >= 15 and age < 18 and prom >= 8.5:
    print("Bachillerato, promedio aceptable")
elif age >= 6 and age < 12 and prom < 8.5:
    print("Bachillerato, promedio triste")
elif age >= 18 and age < 23 and prom >= 8:
    print("Universidad, promedio aceptable")
elif age >= 6 and age < 12 and prom < 8:
    print("Universidad, promedio triste")
else:
    print("Profesionista, tu ya no estudias")
