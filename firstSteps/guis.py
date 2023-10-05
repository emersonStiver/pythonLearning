from tkinter import *

#ROOT
root = Tk()
root.title("First window")
root.resizable(1,1)
root.geometry("650x350")
root.config(bg="blue")

#FRAME
miFrame=Frame()
miFrame.pack(fill="both", expand=True)
miFrame.config(bg="red")
miFrame.config(width="650", height="350")
miFrame.config(bd=10)
miFrame.config(relief="groove")
#miFrame.config(cursor="hand2")

minombre=StringVar()

#LABEL
label1 = Label(miFrame, text="Usuario",font=("Comic Sans MS",18))
#label1.place(x=100,y=200) #pack()
label1.grid(row= 0,column=0)

label2 = Label(miFrame, text="Contraseña",font=("Comic Sans MS",18))
label2.grid(row=1,column= 0)

label3 = Label(miFrame, text="Email",font=("Comic Sans MS",18))
label3.grid(row=2,column=0)

#ENTRIES
entry1 = Entry(miFrame)
entry1.grid(row=0,column=1,sticky= "e",padx = 10, pady=10)

entry2 = Entry(miFrame)
entry2.grid(row=1,column=1,sticky= "e",padx = 10, pady=10)

entry3 = Entry(miFrame)
entry3.grid(row=2,column=1,sticky= "e", padx = 10, pady=10)
entry3.config(fg= "red", justify="right")
entry3.config(show="xxx")

texto = Text(miFrame, width=16, height=5)
texto.grid(row=4,column=1,padx=10,pady=10)


scrollVert = Scrollbar(miFrame,command =texto.yview)
scrollVert.grid(row=4,column=2, sticky="nsew")
texto.config(yscrollcommand = scrollVert.set)

def codigoBoton():
    minombre.set("juan")

botonEnvio = Button(root, text="Envia", command = codigoBoton())
botonEnvio.pack()


root.mainloop()
