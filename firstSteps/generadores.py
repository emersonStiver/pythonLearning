
def generaPares(limite):
    num = 1
    milista = []

    while num < limite:
        milista.append(num*2)
        num = num +1
    return milista

print(generaPares(10))

def generaPares2(limite):
    num = 1
    while num < limite:
        yield num*2
        num= num +1

devuelvePares = generaPares2(10)



print(next(devuelvePares))
print("aqui podria ir mas codigo")
print(next(devuelvePares))
print("aqui podria ir mas codigo")
print(next(devuelvePares))



#YIELD FROM
#SIMPLIFICAR EL CODIGO DE GENERADORES EN EL CASO DE UTILIZAR BUCLES ANIDADOS
def devuelve_ciudades(*ciudades): #el * indica que recibira una cantidad indefinida de parametros
    for elemento in ciudades:
        #for subelemento in elemento:
            yield from elemento
ciudades_devueltas = devuelve_ciudades("bogota", "medellin","florencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
#ahora el yield from nos ayuda a presincidr del segundo for anidado


