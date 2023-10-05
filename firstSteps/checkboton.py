from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root =Tk()

def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de excel", "*.xls"), ("Ficheros de texto", "*.txt"), "Todos los ficheros", "*.*"))
    print(fichero)

def infoadicional():
    messagebox.showinfo("Procesador de Emerson", "Procesador de texto 2024")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia generica")

def salirAplicacion():
    #valor = messagebox.askquestion("Salir", "Desea salir de la aplicacion?")
    valor = messagebox.askokcancel("Salir", "Desea salir de la aplicacion?")
    if valor:
        root.destroy()
def cerrar_documento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
    if valor == True:
        root.destroy()
barraMenu = Menu(root)
root.config(menu=barraMenu)

#elementos que el menu tendra
archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Abrir", command=abreFichero)
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command= cerrar_documento)
archivoMenu.add_command(label="Salir",command= salirAplicacion)

archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas = Menu(barraMenu,tearoff=0)

archivoAyuda = Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acera de", command = infoadicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

#SUBMENU


root.title("El ejemplo")
playa = IntVar()
montana = IntVar()
turismoRural = IntVar()

def opcionesViaje():
    opcionEscogida=""
    if(playa.get()==1):
        opcionEscogida+=" Playa"
    if (montana.get() == 1):
        opcionEscogida += " Montaña"
    if (turismoRural.get() == 1):
        opcionEscogida += " Turismo rural"
    textoFinal.config(text=opcionEscogida)

#foto = PhotoImage(file="avion.png")
#Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Elige destinos",width=50).pack()

Checkbutton(frame, text="Playa",variable=playa,onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña",variable=montana,onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural,onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()
root.mainloop()