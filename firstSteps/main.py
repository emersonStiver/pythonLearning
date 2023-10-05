
#PRACTICE FOR LISTS
lista = ["hola", "soy", "emer", "aprendo" , "python"]
otralista = ["sdf", "adfs"]
print(lista[:2])
print(lista[-3])
print(lista.insert(2, "Sandra"))
lista.extend(["es", "genial"])
print(lista.index("emer"))

print("aprendo" in lista)
lista.remove("aprendo")
lista.remove("es")
lista.pop() #elimina el ultimo elemento de una lista
milista = lista + otralista
print(lista)

#PRACTICE FOR TUPLES
mitupla2 = tuple(lista)
mitupla = ("hola", "soy", "tupla",1 ,2 ,1999, 1999)
tuplaunitaria =("sola", )
a,b,c,d,e,f,g = mitupla
print(mitupla)
print("hola" in mitupla)
print(mitupla.count(1999))

#PRACTICE FOR DICTIONARIES
mydictionary = {"Alemania": "Berlin", "España" : "Madrid", "Francia": "Paris", 23 :"numero"}
mydictionary["italia"]="Lisboa" #adding one more entry
print(mydictionary)
mydictionary["italia"]="roma"
print(mydictionary)
del mydictionary["Alemania"]
print(mydictionary)
mydictionary2 = {milista[0]: "madrid", mitupla[1]: "nose"}
print(mydictionary2)
mydictionary3 = {23: "jordan", "nombre": "michael", "anillos": (19,29,292,29)}#we can do the same thing with a list
print(mydictionary3["anillos"])
print(type(mydictionary3["anillos"]))

print(mydictionary.keys())#returns the keys from the dictionary
print(mydictionary.values())#returns the values

for i in mydictionary.values():
    print(i)
for x, y in mydictionary.items():
    print(x," ", y)
