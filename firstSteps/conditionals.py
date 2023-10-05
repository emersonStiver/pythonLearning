print("verificacion de acceso: ")

edad_usuario = int(input("Ingresa tu edad: "))

if edad_usuario < 18:
    print("no puedes pasar")
elif edad_usuario > 68:
    print("muy viejo")
else:
    print("Puedes pasar")

    #concatenacion de operadores de concatenacion
edad = 7
if 0<edad<100: #si la condicion es cierta, pasa a evaluar edad<100
               #si es falso, salta al else, y no evalua la siguiente condicion
    print("edad es correcta")
else:
    print("edad incorrecta")

if edad <18 and edad_usuario < 54:
    print("ambas condiciones deben ser true para entrar al codigo")

if edad < 18 or edad_usuario < 54:
    print("si la condicion 1 no se cumple, evalua la segunda condicion para ver si es true")

tuples = ("ingles", "Sociales", "creatividad", "matematicas", "fisica")
asignatura = input("Ingresa la materia que quieres ver como optativa: ").lower()
if asignatura in tuples:
    print("la materia " + asignatura + " esta disponible")
else:
    print("La materia " + asignatura +" no esta disponible")


#for, while, LOOPS

for i in ["Pildoras", "Informaticas", 3]:
    print("Hola", end="")#this prints the values in a single line
    #if we add more spaces in end="  " it separates the words by the same amount of spaces
    print(f"valor de la variable {i}") #imprime el vlaor de i, F concatena


for x in range(5, 50, 3): #start, end, increment by 3
    print(x)

email = input("Introduce email")
for y in range(len(email)):
    print(y)
    if email[i] =='@':
        print("email correcto")
counter= 1
while counter > 5 and counter < 100:
    print("contando...")
    counter = counter +1
    break

for i in email:
    if i == '@':
        arroba = True
        break;
else:
    arroba = False
    #this else is executed once the for is done with the iterations
    #so the last thing it does is executing what is inside of the else
    #but during the iteration, it is not run, just at the end