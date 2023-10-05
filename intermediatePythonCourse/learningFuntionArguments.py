#the difference between arguments and parameters
def print_name(name):
    print(name)
print_name("alex")#arguments

#positional and keyword arguments
def foo(a,b,c, d=5):
    print(a,b,c,d)

foo(1,2,3)#positional arguments
foo(a=1, c=3, b=9)#keyword arguments
foo(1, b=2, c=3)#mixed way
foo(1,2,3)#default value, we pass 3, but 4 are required

#variable-length arguments (*args, **kwargs)
def argsAndkwargs(a,b, *args, **kwargs):#args for variable, kawargs for keywords
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
print("args variables")
argsAndkwargs(1,2, 9,8,7,6, three=3, four=4)


#container unpacking into function arguments
def unpack(a,b,c):
    print(a,b,c)
mylist= [0,1,2]
mytuple= (0,1,2)
mydict = {'a':1, 'b':2, 'c':3}
unpack(*mylist)
unpack(*mytuple)#the length of the parameters must match the arguments(list)
unpack(**mydict)


#local vs. global arguments
def globalVariable(x):
    x +=1#this creates a new local variable, and the outside variable is not modified
    number = 0#this creates a local variable, different to the global variable that is outside
#to update it you gotta state !!!!global variableName!!!!
number = 5
globalVariable(number)



#parameter passing (called by value or by reference?) in python is called by object, object reference

#mutable objects like lists, or ditcs can be modified within a function, and the changes will be visible
#outside of the function
def parameterPassing(a_list):
    var2 = 40#this creates a local variable, it doesn't affect the global var2
    #a_list=[200,300,400]#if we rebind a mutable object, the outside object is not affected
    #this is now a local list
    a_list += [200,300,400]#this will change the outside list, because we are concatanating

    a_list.append(4)
    a_list[0]= -100
    x=5


var2 = 10#inmutable type, cannot be changed
my_list = [1,2,3]#mutable type
parameterPassing(my_list)#we can the mutable type
print(my_list)#the mutable object LIST is sent as an argument, some processing occures
#and the list is modified and the chagnes are visible outside of it

#inmutable objects can not be changed within a method, but inmutbale objects contained within a mutable object
#can be changed



#parameters: variables that are defined inside parenthesis or when defining a function
#arguments: values passed for these parameters while calling a function


