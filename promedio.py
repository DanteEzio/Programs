nombre = input("Enter your name: ")
calif_1 = float(input("Enter the first grade: "))
calif_2 = float(input("Enter the second grade: "))
calif_3 = float(input("Enter the third grade: "))

prom = (calif_1 + calif_2 + calif_3) / 3

if prom >= 7:
     print(nombre," you passed with ",prom,",congratulations!")
else:
    print(nombre," you failed with ",prom,",im sorry.")
    
