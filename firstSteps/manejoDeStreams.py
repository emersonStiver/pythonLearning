from io import open

archivo_texto = open("pruebaIo.txt","r+")
#frase ="Dia para estudiar \n el miercoles"
#archivo_texto.write(frase)
#archivo_texto.close()

#texto = archivo_texto.read()
#lineas = archivo_texto.readlines()
#archivo_texto.close()

#archivo_texto.write("\n siempre es una buena ocasion para aprender")

#archivo_texto.seek(11)
#print(archivo_texto.read())

lista_texto = archivo_texto.readlines()
lista_texto[1]= "Esta linea ha sido modificada"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()



archivo_texto.close()