months = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")

selection = "s"
while selection == "s":
    month = int(input("Dame el mes que deseas visualizar: "))
    if month < 1 or month > 12:
        print("Valor incorrecto")
    else:
        month_str = months[month-1]
        print("El mes es: ", month_str)
        selection = input("Quieres ver otro mes? ")
print("Adios")

