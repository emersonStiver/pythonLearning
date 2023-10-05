

class place_of_value_AND_rounding:

    def requestData(self):
        entrada = int(input("Insert a number to be rounded off"))
        length = len(str(entrada))
        return entrada, length

    def arrayOfDigits(self,numero, list, length):

        reminder = numero
        length1 = length
        print(length)
        divided = numero
        listN = []
        desarrollo = True

        while desarrollo:
            divided = int(divided / 10)
            if divided < 10:
                listN.append(divided)
                data_list = int(list[length1 -2])
                divided = reminder - (divided * data_list) #because the index starts with 0, and the operationof the place of value ommits one number because of the multiplication process
                reminder = divided
                length1 = length1-1

                for i in range(9):
                    if reminder == i:
                        listN.append(reminder)
                        desarrollo = False #Por que al poner un break y while: hay un error con la lista en indexes

        print(listN)
        return listN


    def createPlaceOfValue (self, length):
        arr = []
        counter = 1
        for i in range(length - 1):
            counter = (10 * counter)
            arr.append(counter)
        return arr


obj = place_of_value_AND_rounding()
entrada, length = obj.requestData()
obj.createPlaceOfValue(length)
obj.arrayOfDigits(entrada, obj.createPlaceOfValue(length), length)





















