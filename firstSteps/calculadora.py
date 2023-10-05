from tkinter import *

operand = ""
resultado = 0
root = Tk()
miFrame = Frame(root)
miFrame.pack()

#------------VARIABLES---------------

numeroPantalla = StringVar()
subNumeroPantalla = StringVar()


#------------EVENTOS TECLADO----------
def numeroPulsado(num):
        global operand
        if operand != "":
                numeroPantalla.set(num)
                operand = ""
        else:
                numeroPantalla.set(numeroPantalla.get()+num)

def suma (num):
        global operand
        global resultado
        resultado += int(num)
        operand = "+"
        numeroPantalla.set(str(resultado))

        # num1.append(numeroPantalla.get())
        # subPantalla.set(num1 + " + ")
        # num2 = numeroPantalla.get
def resta(num):
        global operand
        global resultado
        resultado -= int(num)
        operand="-"
        numeroPantalla.set(str(resultado))

def multiply(num):
        global operand
        global resultado
        resultado *= int(num)
        operand="*"
        numeroPantalla.set(str(resultado))

def division(num):
        global operand
        global resultado
        try:
                resultado /= int(num)
        except:
                numeroPantalla.set("0")
        operand="/"
        numeroPantalla.set(str(resultado))
def elResultado():
        global resultado
        global operand
        print(operand)
        numeroPantalla.set(str(resultado+int(numeroPantalla.get())))

        resultado = 0

#-------------PANTALLA--------------
subPantalla = Entry(miFrame, textvariable=subNumeroPantalla)
subPantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
subPantalla.config(bg="black", fg="#03f943", justify="right")

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=2, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

#-----------FILA 1-------------------
boton7 = Button(miFrame, text="7", width=3)
boton7.grid(row=3, column=1)
boton7.bind("<Button-1>", lambda event: numeroPulsado("7"))

boton8 = Button(miFrame, text="8", width=3)
boton8.grid(row=3, column=2)
boton8.bind("<Button-1>", lambda event: numeroPulsado("8"))

boton9 = Button(miFrame, text="9", width=3)
boton9.grid(row=3, column=3)
boton9.bind("<Button-1>", lambda event: numeroPulsado("9"))

botonDiv = Button(miFrame, text="/", width=3)
botonDiv.grid(row=3, column=4)
botonDiv.bind("<Button-1>", lambda event: division(numeroPantalla.get()))


#-----------FILA 2-------------------
boton4 = Button(miFrame, text="4", width=3)
boton4.grid(row=4, column=1)
boton4.bind("<Button-1>", lambda event: numeroPulsado("4"))

boton5 = Button(miFrame, text="5", width=3)
boton5.grid(row=4, column=2)
boton5.bind("<Button-1>", lambda event: numeroPulsado("5"))

boton6 = Button(miFrame, text="6", width=3)
boton6.grid(row=4, column=3)
boton6.bind("<Button-1>", lambda event: numeroPulsado("6"))

botonMult = Button(miFrame, text="*", width=3)
botonMult.grid(row=4, column=4)
botonMult.bind("<Button-1>", lambda event: multiply(numeroPantalla.get()))


#-----------FILA 3-------------------
boton1 = Button(miFrame, text="1", width=3)
boton1.grid(row=5, column=1)
boton1.bind("<Button-1>", lambda event: numeroPulsado("1"))

boton2 = Button(miFrame, text="2", width=3)
boton2.grid(row=5, column=2)
boton2.bind("<Button-1>", lambda event: numeroPulsado("2"))

boton3 = Button(miFrame, text="3", width=3)
boton3.grid(row=5, column=3)
boton3.bind("<Button-1>", lambda event: numeroPulsado("3"))

botonSum = Button(miFrame, text="-", width=3)
botonSum.grid(row=5, column=4)
botonSum.bind("<Button-1>", lambda event: numeroPulsado("-"))

#-----------FILA 4-------------------
boton0 = Button(miFrame, text="0", width=3)
boton0.grid(row=6, column=1)
boton0.bind("<Button-1>", lambda event: numeroPulsado("0"))

botonComa = Button(miFrame, text=",", width=3)
botonComa.grid(row=6, column=2)
botonComa.bind("<Button-1>", lambda event: numeroPulsado(","))

botonIgual = Button(miFrame, text="=", width=3)
botonIgual.grid(row=6, column=3)
botonIgual.bind("<Button-1>", lambda event: elResultado())

botonSum = Button(miFrame, text="+", width=3)
botonSum.grid(row=6, column=4)
botonSum.bind("<Button-1>", lambda event: suma(numeroPantalla.get()))


root.mainloop()