
import sys
def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

#for i in g:
    #print(i)
#if it does not reach another yield statement, it'll generate an error
value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)


def countDown(num):
    print("Starting")
    while num > 0:
        yield num
        num -=1
dc = countDown(4)#  nothing is executed until we iterate over the generator
value = next(dc)
value2 = next(dc)
value3 = next(dc)
value4 = next(dc)

print(value4)

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num +=1
    return nums
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num +=1

myList = sys.getsizeof(firstn(100))
myList2 = sys.getsizeof(firstn_generator(100))
print(myList)
print(myList2)

#Fibonachi sequence

def fibnacci(limit):
    #First two numbers are 0 1, the following numbers are a sum of the previous numbers
    a, b = 0,1
    while a < limit:
        yield a
        a, b = b, a +b
        print(str(a) +  "  " + str(b))

fib = fibnacci(12)
for i in fib:
    print(i)

