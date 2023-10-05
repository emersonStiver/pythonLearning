# tuple: ordered, immutable, allows duplicate elements
#used for objects that belong together
#if you wanna create a one element tuple, follow this sintax
# mytuple = ("max",)

mytuple = ("Max", 23, "Boston")
mytuple2 = tuple(["max", 23, "boston"])
print(mytuple2)

item = mytuple[-3]
print(item)

if "Max" in mytuple:
    print("yes")

mytuple3 = ('a','b','c')
amount = len(mytuple3)
print(mytuple3.count('o'))

mytuple3.index('c')#gets the index of the value passed
#slicing in tuple works tbe same way as in list, not including del or chaning

#UNPACKING
name, age, city = mytuple2

tupleNums = (0,1,2,3,4,5,6,7,8,9)

n1,  *n2, n3 = tupleNums
print(n1)
print(n2)
print(n3)


#MORE EFFICIENT THAN LISTS