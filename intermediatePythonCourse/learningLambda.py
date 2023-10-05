#anonymous function,     lambda arguments: expression
#it creates a function, evaluates the expression and return the result
from functools import reduce
add10 = lambda x: x+10
print(add10(5))

mult = lambda x, y : x*y
print(mult(4,6))

#they are used when you need a fucntion that is only used once in your code
# or in functions that take another function as an argument, for example
# used along with the built in
#function map() sorted() filter() reduce()

def sort_by_y(x):#this function can also be passed as a parameter in the lambda
    return x[1]

points2D = [(1,2),(15,1),(5,-1),(10,4)]
points2d_sorted = sorted(points2D, key=  lambda x: x[1]    )#it also takes a function for the key value
print(points2D)
print(points2d_sorted)


a = [1,2,3,4,5]

b = map(lambda x: x*2, a)
print(list(b))
c = [x*2 for x in a]
print(c)

t = filter(lambda x: x%2==0, a)
print(list(t))
tt = [y for y in a if y%2==0]
print(tt)

#reduce(func, seq)
product_a = reduce(lambda x,y: x*y,a)
print(product_a)