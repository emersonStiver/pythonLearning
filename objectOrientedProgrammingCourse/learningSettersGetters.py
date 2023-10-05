from Item import Item
from Phone import Phone

#GETTERS AND SETTERS
#We can create readonly values, so we can only change them when instanciating
#restrict users from overwriting values after initialization

item5 = Item('computer', 123000, 10)
print(item5.name)
item5.name = 'other name for computer'
print(item5.name)
print(Item.nItems)
print(item5.quantity)