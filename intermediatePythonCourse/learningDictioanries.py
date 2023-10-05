#Dictionary: key-value pairs, unordered, mutable

mydict = {"name": "max", "age": 28, "city": "florencia"}

mydict2 = dict(name="max", age=24, city="boston")

value = mydict["city"]#access one value by passing the key

mydict["city"]= "berlin"#changing the value of one key
print(mydict)

mydict["email"] = "emersonstiven1@gmail.com"
print(mydict)


#DELETE ITEMS
del mydict["name"]

mydict.pop("age")

mydict.popitem()#removes the last inserted item

print(mydict)

try:#if the value is not found, it throws an exception
    if "name" in mydict:
        print(mydict["name"])
    else:
        print("doesn't exist")
except:
    print("error")


#ITERATION

for value in mydict.values():
    print(value)
for key in mydict.keys():
    print(key)
for key, value in mydict.items():
    print(key + " " + value)

#CREATING A COPY

copydic = dict(mydict)
copydic2 = mydict.copy()

#MERGING TWO DICTIONARIES
mydict.update(mydict2)#the key-value pairs shared in both dicts are overwritten
#by the key-value pairs contained in the dict passed as an argument
print(mydict)

#use a tuple as a key
mytuple = (9,2)
anotherDic = {mytuple: "numeros"}
print(anotherDic)