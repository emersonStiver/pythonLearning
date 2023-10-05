#SETS: unordered, mutable, no duplicates
myset = {1,2,3,4,5,6,7,8,9}
myset2 = set("hello")
myset3 = set()

myset.add(1)
myset.add(8)

myset.remove(1) #no element found, raises an error
myset.discard(3)#removes the element, if no elem found, does not raise an error
myset.pop()#removes any number from the set, and returns it

if 1 in myset:
    print("yes")
print(myset)


#unions
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
prime = {2,3,5,7}

u = odds.union(evens)
print(u)

i = odds.intersection((prime))#prints the intersected elements
print(i)

seta = {1,2,3,4,5,6,7,8,9}
setb = {1,2,3,10,11,12}

diff = seta.difference(setb)#prints elements missing in set b
print(diff)

diff2 = setb.symmetric_difference(seta)#prints elements that are in both sets
print(diff2)

#MODIFYING
print("Modifying")
seta.update(setb)#update the elements in set a by including those not duplicated from set b
print(seta)
seta.intersection_update(setb)#updates the elements with those elements found in both sets
print(seta)

#super SETS

setA = {1,2,3,4,5,6,7}
setB = {1,2,3}
print(setA.issubset(setb))#if all elements of seta are in set b

print(setB.issuperset(seta))#setb contains all alements from set a

print(setA.isdisjoint(setB))#returns false because set a has the same elements, so there is no intersection

#creating a copy

copi = setA.copy()
copo2 = set(setA)

#frozen set: immutable form of a set

a= frozenset([1,2,3,4])