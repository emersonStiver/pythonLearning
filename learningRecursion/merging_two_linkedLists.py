# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)
class Linked_list:
    def __init__(self):
        self.head = None
    def add(self, data):
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode#so the previous node reference will be saved here and given to the next one, so the new element
        #will point to the previous element


linlist1 = Linked_list()
linlist1.add(1)
linlist1.add(2)
linlist1.add(4)


linlist2 = Linked_list()
linlist2.add(1)
linlist2.add(3)
linlist2.add(4)

def mergeTwoLists( list1, list2):
    storage = []
    increment = 0
    insertion = list2.head
    head1 = list1.head
    while True:
        storage.append(insertion)
        insertion = insertion.next
        increment +=1
        if insertion == None:
            break
    merge(head1, storage, 0)
    return list1.head



def merge(following, insertions, counter):
    if counter > len(insertions)-1:
        return
    current = following
    nextObject = following.next

    current.next = insertions[counter]
    insertions[counter].next = nextObject
    merge(nextObject, insertions, counter+1)

def show(head):
    current = head
    while True:
        print(current)
        if current.next == None:
            break
        current = current.next


mergeTwoLists(linlist1, linlist2)

