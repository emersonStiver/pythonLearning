#STRINGS: Ordered, immutable, text represetation
import string
from keyword import iskeyword

my_String = "  Hello woH hellohelloe helloe HHrlmH  "
my_String2 = 'otro gato'
my_String3 = """hellosfsdf
asdfsdfsd
sdfdf
            """

print(my_String3)

char = my_String[0]#prints the first character in the string
#SLICING
subString = my_String[1:5]
print(type(subString))
combined = my_String + " " + my_String3# concatanates both strings


if 'h'  in my_String:
    print("yes")

removingSpaces= "              hello world"
print(removingSpaces.strip())
#STRINGS ARE UNMUTABLE, SO WE ALLOCATE THE STRING IN A NEW STRING
#OR WE CAN CHANGE HOW THEY ARE DISPLAED, BUT THE ORIGINAL, WILL NOT BE CHANGED


print(my_String.casefold())
print(my_String.center(200,'-'))
print(my_String.count("H", 0,3))
print(my_String.endswith(("m","H"), 1,))#it can be a tuple or another string
print(my_String.find('H', 4,len(my_String)))#first occurance
print(my_String.rfind("H",4,len(my_String),))#last occurance
print("")
print(my_String.isalnum())#there can not be whitespaces
print(my_String.isalpha())
print(my_String.isidentifier())
print(iskeyword(my_String))
print(my_String.islower())
print(my_String.isnumeric())
print(my_String.isspace())
unav = "     uno"
dosv="dos"

print("")
print("PRUEBA DE JOIN METHOD")
print("")

listtobeconcatenated = "hellow my name is emerson the programmer".split()
stringtobejoined="hello i am mar  celo mu  rcia"
print(' '.join(listtobeconcatenated))

listForJoin = ['a']*6
print(listForJoin)

#bad practice to group elements of a list into a string again
finalStringForJoin = ''
for i in listForJoin:
    finalStringForJoin += i#passes each element in the list to the string variable


#good usage of the join method
finalJoin = ''.join(listForJoin)
print(f'good use of join method {finalJoin}')

print(unav.lstrip(' '))#removes the leading characters .
print(unav.rstrip(' '))#removes the trailing characters .
print(my_String.strip())

print(my_String.removeprefix('Hello '))#removes just the first occurance passed as a parameter

s = "hello world"
tranlation_table = s.maketrans("world", "12345")
print(s.translate(tranlation_table))

translation_table2 = s.maketrans("","", "o")
print(s.translate(translation_table2))

print(my_String.partition(" "))
print(my_String.rpartition(" "))
print(my_String.replace("he", "GE",1))

print(my_String.rsplit(' '))
print(my_String.swapcase())
print(my_String.title())
print(string.capwords(my_String))#it only considers whitespaces


alista = "how are you doing man?"



#FORMATTING
#OLD WAY WITH THE .FORMAT() METHOD

var = "Tom"
anotherString = "The variable is %s"% var

varN = 2
secondString = "The variable is %d" % varN

varF = 4.0343434234324
thirdString ="The variable is %.2f" % varF


#NEW WAY f-Strings
fourthString = "The variable is {:.2f} and {}".format(varF, varN)
fithString = f"The variable is {var*2} and {varN}"

