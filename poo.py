"""Recibe del teclado la siguiente informacion de una persona: Nombre, Apellidos, Edad, Estatura y Peso. Una vez con los datos, crea una clase llamada Perosna, cuyos atributos serán los mencionados anteriormente. La idea es que cuando tengas los datos ya guardados en variables, puedas crear una instancia de la clase con dichos datos. Crea en la clase un metodo que te permita mostrar el nombre completo de la persona, así como otro método para calcular su IMC"""

class Person:
    def _init_(self, name, last_name, age, height, weight):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight

    def get_full_name(self):
        print(f'Nombre completo: {self.name} {self.last_name}')
    
    def calculate_imc(self):
        imc = (self.weight / self.height ** 2)
        print("Tu IMC es : ", imc)

name = input("Dame tu nombre: ")
last_name = input("Dame tus apellidos: ")
age = input("Dame tu edad: ")
height = float(input("Dame tu altura: "))
weight = float(input("Dame tu peso: "))

person = Person(name, last_name, age, height, weight)

person.get_full_name()
person.calculate_imc()

