class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("me desplaza utilizando 6 ruedas")

#normally, if we wanted to use the desplazamiento() method from each class
#we would need to instantiate the class and call the method
micoche = Coche()
micoche.desplazamiento()
mimoto = Moto()
mimoto.desplazamiento()
camion = Camion()
camion.desplazamiento()

#but, there is another way,

#def desplazamiento(vehiculo):
    #vehiculo.desplazamiento()

#desplazamiento(camion)