import json

#CONVERTING A DICTIONARY INTO A JSON OBJECT
person = {"name": "john", "age": 30,  "city": "new york", "hasChildren": False, "titles": ["engineer", "programmer"]}
personJson = json.dumps(person , indent=4, sort_keys=True )

#WRITING A JSON FILE WITH BASED ON A DICTIONARY
with open ('person.json', 'w') as file:
    json.dump(person, file, indent=4)

#READING THE CONTENT OF THE JSON FILE
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)

#DESERIALIZATION OF THE JSON FILE INTO THE PYTHON OBJECT
person = json.loads(personJson)
print(person)





#SERIALIZING OBJECTS INTO JSON OBJECTS

#A NORMAL CLASS CALLED USER
class User:
    def __init__(self,name, age):
        self.name = name
        self.age = age
#this alone throws an error
user = User('Max', 28)

#First way to serialize objetcs into JSON
#We have to define an ENCODER OBJECT for the objects we want to parse to JSON
def encode_user(o):#it states how to encode the object
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        else:
            raise TypeError("object of type ")

#Second way to serialize objects into JSON
#We import JSONEncoder and define a class that contains the default method
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self,o)


userJson1 = json.dumps(user, default=encode_user)#first way
userJson2 = json.dumps(user, cls=UserEncoder)#second way

#Third way to serialize objetcs into JSON
userJson3 = UserEncoder().encode((user))
print(userJson1)
print(userJson2)
print(userJson3)


#DESERIALIZING JSON OBJECTS INTO PYTHON OBJECTS
#We have to follow the same procedure and create a decoder method

def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict['name'], age=dict['age'])
    return dict
#we are using one of the 3 json objects created in the serialization process
userDecoded = json.loads(userJson1, object_hook=decode_user)
print(type(userDecoded))
print(userDecoded)
print(userDecoded.name)
print(userDecoded.age)






