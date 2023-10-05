import csv

class Item:
    #These are class attributes
    pay_rate = 0.8
    nItems = 0
    listItems = []

    #-we can have default attributes if we don't know the value of the attribute beforehand
    #-we can specify the data type that each parameter needs to receive when it is instanciated
    def __init__(self, name: str, price : float, quantity=0):
        #Assert allows to validate the arguments and catch errors when creating an instance

        assert price >= 0, f'Price {price} is not equal or greater than zero!!!'
        assert quantity >=0

        #These are instance attributes
        self.__name = name
        self.price = price
        self.__quantity = quantity

        #Actions to execute when creating an instance
        Item.nItems = self.nItems +1
        Item.listItems.append(self)

    @property #read only attribute
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def quantity(self):
        return self.__quantity


    def cal_total_price(self):
        return self.price * self.__quantity

    def apply_discount(self):
        #we can access pay_rate from the class or the instance like Item.pay_rate or self.pay_rate,
        # Best practice is self.pay_rate because if we change the class attribute in running time,
        # the change will not be visible in the instance level
        self.price= self.price * self.pay_rate

    #Decorator creates a class method
    @classmethod
    def instantiate_from_csv(cls):#receives the class itself as argument
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for x in items:
            print(x)
        for y in items:
            Item(
                name = y.get('name'),
                price = int(y.get('price')),
                quantity = int(y.get('quantity'))
            )
    @staticmethod#staticmethods don't require an instance of the object,we never send the object as the first argument
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    @classmethod
    def numberInstances(self):
        return self.nItems

    def __repr__(self):
        return f'{self.__class__.__name__}(name : {self.name} price: {self.price} quantity: {self.__quantity} )'


#as we have the quantity attribute by default, we are not obliged to pass an argument
item1 = Item('phone', 1000000)
item2 = Item('charger', 30000, 1000)
item3 = Item('headphones' ,200000, 100)

#we can add attributes after the creation of the item
item1.has_cable = True


#print(item1.pay_rate) #accessing through the instance
#print(Item.pay_rate) #accessing through the class

#print(item1.__dict__)#Magic method, returns all adributes

#print(item1.price)#price variable is 1000000
#item1.apply_discount()#disscount applied
#print(item1.price)#variable is set to 800000


#Item.instantiate_from_csv()#the Item class is pass as argument, not an instance of the class
#which is done with the self parameter

#print(Item.numberInstances())
#print(Item.listItems)





#figure out how does the passing of arguments in a class, if values are updated or not!!!


