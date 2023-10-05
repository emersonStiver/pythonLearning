#lists: ordered, mutable, allows duplicate elements

myList = ["banana", "pera", "apple", "apple"]#duplicate elements

myList2 = [2,3,5,6,7,75,5]
del myList2[0]#the first element is gone


item = myList[0]
for i in myList2:
    print(i)

myList.insert(1, "perraaa")
itemRemoved = myList.pop()
itemR2 = myList.remove("apple")

item3 = myList.reverse()
item4 = myList2.sort()
newList = sorted(myList)
print(myList2)
print(myList)

combinedList = myList + myList2

#a = myList[1:5]
#a = myList[:3]
#a = myList[2:]
a = myList2[::2]#step index all the way to the end with one step
print(a)



#SLICING------------------ The full slice syntax is: start:stop:step
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]

num2 = nums[-4:-1]
num3 = nums[:-3]
num3 = nums[1:-3-2]
reveredList = nums[::-1]
reveredList = nums[-1::-1]#builds a reversed list that starts at index -1, so 90 is left out
reveredList = nums[-2:2:-1]#in addition to the previous syntax, now it stops at index 2
print(reveredList)
print(num3)

five_items_after_second = slice(2,2+5,2)#slice function
newNumList = nums[five_items_after_second]
all_but_two_last = slice(None, -2)
unalista = nums[all_but_two_last]
print(unalista)


#SLICE ASSIGNMENT
nums[:4] = ["Hemos", "cambiado", "de"]
nums[:4] = [1,2,3,4,5,6,7,8,9,10]
print(nums)

# SLICE DELETION
del nums [3:7]#we can remove a slice out of a list
print(nums)

#LIST COMPREHENSION   newlist = [expression for item in iterable if condition == True]

aaa = [1,2,3,4,5,6,7]
b = [i *i for i in aaa]
listClients = ["emer","danna","jorge","humberto", "sayan"]
clients = [x.upper() for x in listClients if "h" in x]
print(clients)
#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
fruits = ["banana", "pera", "orange", "sandia", "guanabana" ]
newFruts = [x if x != "banana" else "orange" for x in fruits]
print(newFruts)

#"Return the item if it is not banana, if it is banana return orange".