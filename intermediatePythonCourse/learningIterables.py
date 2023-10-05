#ITERATORS: product, permutations, combinations, accumulate, grouby and infinite iterators

from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, repeat, cycle
from itertools import chain
from itertools import dropwhile
from itertools import filterfalse, islice, takewhile, zip_longest
import operator


#PRODUCT  itertools.product(*iterables, repeat=1)
a = "123"
b = "ab"

prod = product(a,b, repeat=1)
print(list(prod))


#retuns all possible orderings of an input PERMUTATIONS
perm = permutations(a)
print(list(perm))


#COMBINATIONS WITH A SPECIFIED LENGTH
aa = ['A','L','P']
comb = combinations(aa, 2)
print(f'Combinations: {list(comb)}')

comb_wr = combinations_with_replacement(aa,2)
print(list(comb_wr))


#accumulate
aaa = [1,2,3,4]
acc = accumulate(aaa)#func= operator.mul    //   , func=max
print("ACCUMULATE: " + str(list(acc)))


#groupby function, makes an iterator that returns keys from an iterable
def smaller_than_3(x):
    return x<3

group_obj = groupby(aaa, key=lambda x: x<3)#key=smaller_than_3
for key, value in group_obj:
    print(key, list(value))

persons = [dict(name="max", age=25 ), dict(name= "dann",age=25), dict(name="emer", age=27), dict(name="claire", age=28)]
group_obj2 = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj2:
    print(key, list(value))



#chain iterable
#returns an iterator that contains all the elemenets from the iterables
#as if they were all concatanated
qq = [1,2,3]
ee = ['a','b','c']

for i in chain(qq, ee):
    print(i)



#COUNT ITERATOR
#for i in count(2, 10):
    #print(i)



#CYCLE ITERATOR
ccc = [1,2,3]
#for x in cycle(ccc):
  #  print(x)


#REPEAT ITERATOR
for u in repeat("repetitions", 4):#number to be repeated, the amount of times
    print(u)


#DROPWHILE
def is_negative(x):
    return x<0
numbers = [3,-2,5,-6,8,-1,0,-3]
## Drop elements from the iterable until the predicate is false
filtered_numbers = dropwhile(is_negative, numbers)
print(list(filtered_numbers))

#filterfalse:   Make an iterator that filters elements from iterable
# returning only those for which the predicate is False
filtered_numbers2 = filterfalse(is_negative, numbers)
print(list(filtered_numbers2))


words = ['this', 'is', 'a', 'sentence','this', 'is', 'another','sentence']
grouped_words = groupby(words, key=lambda x: x[0])
#for keys, group in grouped_words:
    #group_list = list(group)
    #print(keys, group_list)

#ISSLICE Make an iterator that returns selected elements from the iterable
#itertools.islice(iterable, start, stop[, step])
numeros = [0,1,2,3,4,5,6,7,8,9,10]
filtered_numbers3 = islice(numeros, 1, 8, 3)
print(list(filtered_numbers3))


#takewhile(predicate, iterable)   make an iterator that returns elements from the iterable
#as long as the predicate is true

filtered_numbers4 = takewhile(lambda x: x<5, numeros)
print(list(filtered_numbers4))


#itertools.zip_longest(*iterables, fillvalue=None)
names = ["sara","eduardo", "monica"]
birthdays = [10,45,45]
time_service= [1,23,4]
filtered_longest = zip_longest(names, birthdays, time_service, fillvalue=None)
print(list(filtered_longest))