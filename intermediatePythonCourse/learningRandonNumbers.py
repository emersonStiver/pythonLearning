import random
import numpy as np
import secrets#used for passwords, security tokens, account authentication

w = secrets.randbelow(10)#range from 0 to 10, 10 is not included
z = secrets.randbits(4)#means it can have 4 random binary values
listSecret = list("IDFSIDF")
ll = secrets.choice(listSecret)#secret choice
nump = np.random.rand()#creates an array with randon numbers
nump2 = np.random.randint(0,10, (3,4)) #range 0-10 3 rows and 4 columns

#It is used to generate suble radomn numbers

iint = random.random()#in the range from 0 to 1


aaa = random.randint(1,10)
bbb = random.randrange(1,10)#10 is not included
print("here"+ str(bbb))

cc = random.normalvariate(0,1)
#functions to work with sequences
myList = list("ABCDEFGHI")
ddd = random.choice(myList)#this will pick a random element
eee = random.sample(myList, 3)# picks multiple elements, it will pick unique elements
fff = random.choices(myList, k=3)#this option picks multiple elements, but can be repeated

random.shuffle(myList)#this will shuffle the list
#they are suble radonm numbers



#we can use the seed to reproduce the data with the random functions
#they are not recomended for security purposes
random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))
