import copy
#shallow VS deep copy
#copies of custom objects

org = 5
cpy = org#this doesn't make a copy, it just creates a new varible that points to the same number


orgList = [0,1,2,3,4]
cpyList = orgList#this doesn't create a copy

cpyList[0] = -10

print(orgList)
print(cpyList)

#showllow copy: on level deep, only references of nested child objects
#deepcopy = full independent objects

orgCopies = [0,1,2,3,4,5]
cpyCopies = copy.copy(orgCopies)#shallow copy
cpyCopies2 = orgCopies.copy()#shallow copy
cpyCopies3 = orgCopies[:]#shallow copy
cpyCopies4 = list(orgCopies)#shallow copy
#shallow copies work fine if our element is only 1 level deep

#but let's say, we have a nested list, a list inside a list for example
nestList = [[0,1,2,3,4], [5,6,7,8,9], [10,11,12,13,14]]
#nestCopy = copy.copy(nestList)#this will create a shallow copy, and the original
#sublists will also be affected

nestCopy = copy.deepcopy(nestList)#this will create a copy of the nested objects as well
nestCopy[0][1] = -10
print(nestList)
print(nestCopy)


#for custom objects, like the following
class Person:
    def __init__(self, name, agel):
        self.name = name
        self.age = agel
p1 = Person('alex', 23)
p2 = copy.copy(p1)#we copy a customized object

#the original person doesn't get affected
p2.age = 28
print(p2.age)
print(p1.age)

#but if we have a deeper level
print("------------")
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee
deeperPerson1 = Person('danna', 22)
deeperPerson2 = Person('nubia', 53)

company = Company(p1,p2)
company_clone = copy.copy(company)#shallow compy
company_clone.boss.age = 34#through the shallow copy, we try to change
#the age of the boss and assign someting new

#this will also update the variable age for the original object
print(company_clone.boss.age)
print(company.boss.age)

#to solve this we can use deepcopy()


