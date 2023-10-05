class coche:
    def __init__(self):
        self.ruedas= 4
        self.__anchochasis = 120 #encapsulacion
        self.__largochasis = 250#it's not accessible from outside of the class
        self.__arranchar = False
        self.gasolina = 100
        self.aceite = 40
        self.puertasCerradas = 4
    def show(self):
        print(self.__ruedas)

    def arrancar(self, estado):
        if self.__chequeo_interno():
            print("Puede arrancar")
        else:
            print("Chequeo fallido")
        self.arrancar = estado

    def __chequeo_interno(self):
        estado = True
        print("Realizando chequeo interno")
        if self.gasolina < 30:
            estado = False
            print("Bajo nivel de gasolina")
        else:
            print("Gasolina ok")
        if self.puertasCerradas <4:
            estado = False
        else:
            print("Puertas cerradas")
        if self.aceite <35:
            estado = False
        else:
            print("Aceite ok")
        return estado

class vehiculos:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera =False
        self.frena= False

    def __arranchar(self):
        self.enmarcha = True
    def __acelerar(self):
        self.acelera = True
    def frenar(self):
        self.frena = True
    def estado(self):
        print("Marca: " + self.marca + " Modelo: " + str(self.modelo))

class furgoneta(vehiculos):
    def carga(self,cargar):
        cargado = cargar
        if cargado:
            print("La furgoneta esta cargada")
        else:
            print("la furgoneta no esta cargada")


class Moto(vehiculos):#HERENCIA, HEREDAOS ATRIBUTOS Y FUNCIONALIDADES
    hcaballito="En dos ruedas"
    def caballito(self):
        hcaballito ="voy haciendo el caballito"
    def estado(self):
        print(self.hcaballito)

class veElectricos():
    def __init__(self, marca, modelo):
        super().__init__(self, marca, modelo)
        self.autonomia =100

        def cargarEnergia(self):
            self.carcando = True
class BiciletrasElectricas(veElectricos, vehiculos):#herencia multiple
    pass
miBici = BiciletrasElectricas()#se le da preferencia al costructor y metodos que esta a la izquiera

miMoto = Moto("Honda", 2012)
miMoto.caballito()
miMoto.estado()

miFurgoneta = furgoneta("Renault", "kangoo")
miFurgoneta.carga(True)




carro = coche()
carro.arrancar(True)


#USO DE LA FUNCION SUPER
class persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre =nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):

        print("Nombre: " + self.nombre + " Edad: " + self.edad + " Residencia: " + self.residencia)

class Empleado(persona):

    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residenciaEmpleado):
        super().__init__(nombreEmpleado,edadEmpleado, residenciaEmpleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: "+self.salario, +"Antiguedad: "+ self.antiguedad)

persona1 = persona("Emer", "23", "Colombia")
empleado1 = Empleado(1000000,10,"juan",23,"Caqueta")

print(isinstance(empleado1, persona))


#principio de sustitucion //// es siempre un/a
#un empleado es siempre una persona
#un carro no es siempre una persona XXXX
