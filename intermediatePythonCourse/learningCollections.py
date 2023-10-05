
#collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque
#A Counter is a subclass of dictionary that is used to count the occurrences of items in a collection
a = "aaaaaabbbbcccc"
my_counter = Counter(a)
print(my_counter)

#most_common retuns a tuple, so we can access the elements of the tupple by specifying [] or []
print((my_counter.most_common(1)[0][0]))#how many most common elements are in the dictionary

print(list(my_counter.elements()))

#-------------namedtuple----------------
Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt)
print(pt.x, pt.y)


#----------OrderedDict-----------
#it remembers the order in which elements were inserted
#it was deprecated, because new python version DICT remembers the order
ordered_dict = OrderedDict()


#------------defaultDict-----------
#it will have a default value type if the key has not been set yet
d = defaultdict(int)
d['a']=1
d['a']=3
print(['c'])#with a nromal dict, this line would raise an error
#in this case, it retuns 0 if the key value is int, (varies depending the value)


#-------deque----------------
deq = deque()

deq.append(1)
deq.append(2)
deq.append(3)
print(deq)
print(deq.popleft())
deq.appendleft(5)
print(deq)
deq.pop()#removes the last element
deq.popleft()
print(deq)
#deq.clear()
deq.extend([4,5,6])
deq.extendleft([8,9,0,6])
print(deq)

print(deq.rotate(1))    #the elements rotate to x direction by the amount of time specified in the parameter

