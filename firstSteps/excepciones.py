

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError: #esta solo captura este error, si sucede otro, caeria el progrma de igual manera
    #except:
        print("divdided by 0")
    except ValueError:
        print("input incorrect")
    finally: # it's executed no matter what, doesn't matter if there is an error or not
        print("Calculo se realizo luego del try, o luego de atrapar el error")


#LANZAR EXCEPCIONES/ INSTRUCCION RAISE

class MiPropioError:
    pass
def evalua_edad():
    alert = True
    while alert:
        edad = int(input("Ingreasa tu edad: "))
        if edad <= 0 or edad>100:
            try:
                raise MiPropioError
            except:
                print("Error,valor 0 ingresado o edad mayor a 100")

        dictionary = {range(1,20): "Eres muy joven", range(20,40): "Eres joven",range(40,65): "Eres maduro", range(65,101): "Cuidate..."}
        for i,y in dictionary.items():
            if edad in i:
                print(y)
                alert = False
evalua_edad()