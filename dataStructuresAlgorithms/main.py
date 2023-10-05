#LINEAR SEARCH
#numbers=[2,4,5,2,2,44,6,8,8,6,4,2,34,4]

def linear_search(list, target):
    """returns the index position of the garget
    until the target is found"""
    for x in range(0, len(list)):
        if list[x] == target:
            return x
    return None

def verify(index):
    if index is not None:
        print(f'Target found at index: {index}')
    else:
        print('Target not found in list')

#result= linear_search(numbers, 6)
#verify(result)




def binary_search(numbers, target,first, last ):
#when we use recurssion, and we call the same function in my function, the value returned is returned to the original function
    first = first
    last = last
    mid = (first+last) // 2
    if numbers == None:
        return None
    while first<=last:
        if numbers[mid] == target:
            return mid
        if numbers[mid] < target:#increases to the right
            return binary_search(numbers, target, mid+1, last)
        elif numbers[mid] > target:#decreases to the left
            return binary_search(numbers, target, first, mid-1)
    return None

numbers=[12,9,5,2,44,8,6,4,3,7]
numbers.sort()
target =12
#print(binary_search(numbers, target, 0, len(numbers)-1))

#ARRAYS

new_list = [1,2,3] #values are stores elsewhere, the array only keeps a reference to them
result = new_list[0]

#that's why we run into the errror out of index, because it's trying to access an addrees that
#doesn't exist

#CREATING A LIST

class Node:
    """
    An object for storing a single node of a linked list
    Models two attributes and data and the link to the next list
    """
    data = None
    next_node = None
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return '<None data: %s>' %self.data

class LinkedList:#only head that the list will have

    def __init__(self):
        self.head = None

    def in_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current:
            count = count +1
            current = current.next_node
        return count

    def add(self, data):
        """add new data to the head of the list"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        #  l.add(1)
        #  add(1) will point to the head
        #  add(1) will be stored in the head

        #  add(2) will point the head
        # as add(1) is set in 'head'
        #when we create a new node, it points to the previous node
        #and the self.head variable is set with the new node
        #the first node created is set to the initial value of head
        #which is None
        """node is pointing to the head, and the last node added
        is also pointing to the head"""

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    def show(self):
        current = self.head
        while True:
            print(current)
            if current.next_node == None:
                break
            current = current.next_node
    def insert(self, data, index):
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -=1
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node
    def remove (self, key):
        current = self.head
        previous = None
        found = False
        #if current false, means, tail was found, AND
        #found will be true when the element is found
        while current and not found:
            #this evaluates the possibility that is in the first index
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
            else:
                previous = current#we keep a reference to the previous node, before using current.next_node
                current = current.next_node
        return current




#n1 = Node(10)

#n2 = Node(20)
#n1.next_node =n2
#print(n1.next_node)

l = LinkedList()

l.add(0)
l.add(4)
l.add(2)
l.add(6)
l.add(8)
l.add(3)
l.show()
l.insert(123, 3)
l.size()

print(l.search(0))
print("")
l.show()



