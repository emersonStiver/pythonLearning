import pickle

lista_nombres= ["Pedro","ana","maria","isabel"]
fichero_binario = open("lista_nombres","wb")
pickle.dump(lista_nombres, fichero_binario)
fichero_binario.close()

fichero = open("lista_nombres", "rb")
lista = pickle.load(fichero)
print(lista)

class Vehiculo():
    def __init__(self, brand):
        self.brand = brand
    def brandCar(self):
        print(self.brand)

car1 = Vehiculo("ford")
car2 = Vehiculo("bmw")
car3 = Vehiculo("nissan")
listCars =[car1, car2, car3]

ficherobinario2 = open("losCoches", "wb")
pickle.dump(listCars, ficherobinario2)
ficherobinario2.close()

fichero2 = open("losCoches", "rb")
lista2 = pickle.load(fichero2)
for i in lista2:
    i.brandCar()

class Persona:
    #Global variable, common to all instances
    personas = []
    def __init__(self, name, age, residency):
        self.name = name
        self.age = age
        self.residence = residency

    def mostrarInfo(self):
        print("Name: "+self.name+" Age: " + str(self.age)+" Residence: "+self.residence)

    def guardarEnLista(self, p):
        self.personas.append(p)

    def guardarEnFichero(self):
        ficheroPersonas = open("personasF", "wb")
        pickle.dump(self.personas, ficheroPersonas)
        ficheroPersonas.close()
        del (ficheroPersonas)
        self.mostrarFichero()

    def mostrarFichero(self):
        ficheroPersonas = open("personasF", "rb")
        lista = pickle.load(ficheroPersonas)
        for i in lista:
            i.mostrarInfo()


persona1 = Persona("emer", 23, "florencia")
persona1.guardarEnLista(persona1)
persona1.guardarEnFichero()

persona2 = Persona("danna", 22,"florencia")
persona2.guardarEnLista(persona2)
persona1.guardarEnFichero()


class Empleado(Persona):
    def __init__(self, puesto, salario, nombre, edad, residencia):
        super().__init__(nombre, edad, residencia)
        self.puesto = puesto
        self.salario = salario

empleado1 = Empleado("Cajero",1000000, "Eduardo", 24, "florencia")
empleado1.guardarEnLista(empleado1)
empleado1.guardarEnFichero()



