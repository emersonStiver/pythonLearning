#* multiplication, creation of list or tuples with repeated elemnets
#args, kawrgs, unpacking containers, merging container into a list,
#or merging container into a list, or merging into dictionaries


result= 2*4
power = 2**4#power of fourth
print(result)

zeroes = [0, 1,3]*15
zeroe ="AB"*10
print(zeroes)

#ARGS KWARGS
def learningArgsKargs(a,b,c, *args, **kwargs):
    print(a, b, c)
    for arg in args:#prints the elements of args that are contained inside of it as a tuple
        print(arg)
    for key in kwargs:
        print(key, args[key])

dictt = {'a':1, 'b':2, 'c':3}#we can also pass this with positional arguments, but the length and
# the values have to match between the dict and the parameters of the function

listtt = [39.3,343,34,32,1,6]#we pass listtt with a * to unpack the list into the args
#it also works if the positional parameters match the list's length

learningArgsKargs(2,34,5, *listtt, dictt )
learningArgsKargs(2,34,5, *listtt, dict(seven=4, eight=8))




#unpacking multiple items into a list using *
numbers = [1,2,3,4,5,6]
beginning, *last = numbers
beginning, *middle, last = numbers
beginning, *middle, seconLast, last = numbers
*beginning, last = numbers#it unpacks all elements but the last one
print(beginning)
print(last)




#merge iterables into a list
mytuple = (1,2,3)
myset = {4,5,6}
mylist2 = [7,8,9]

#i can also merge two dictionaries
dictA = {'a':1, 'b':2}
dictB = {'c':3, 'd':4}

new_dict = {**dictA, **dictB}
print(new_dict)
new_List = [*mytuple, *myset, *mylist2]
print(new_List)



