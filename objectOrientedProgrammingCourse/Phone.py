#comma separated values
from Item import Item

class Phone(Item):
    def __init__(self, name: str, price, quantity, broken):
        super().__init__(name, price, quantity)
        self.broken = broken

phone1 = Phone('huawei', 1000,10, True)
phone1.broken_phones = 1

phone2 = Phone('samsung',1200,100, False)
phone2.broken_phones = 1

print(Item.numberInstances())
print(Item.listItems)






