from random import *

def binarysearchI(a, x):
    low = 0
    high = len(a)-1
    mid = (high+low)//2
    if a[mid]== x:
        return mid
    if a[mid] < x:
        while low < high:
            low = mid +1
            if a[low] == x:
                print("List a: "+ str(a) + " value: "+ str(x) +  " length array: " + str(len(a)-1) + " Positioned at: " + str(low))
                return low
            elif a[low] > x:
                a.insert(low, x)
                print("List a: "+ str(a) + " value: "+ str(x) +  " length array: " + str(len(a)-1) + " Positioned at: " + str(low))
                return low
            mid = mid + 1
        a.insert(high+1, x)
        print("List a: "+ str(a) + " value: "+ str(x) +  " length array: " + str(len(a)-1) + " Positioned at: " + str(high+1))
        return high+1

    else:
        while low < high:
            high = mid - 1
            if a[high] == x:
                print("List a: "+ str(a) + " value: "+ str(x) +  " length array: " + str(len(a)-1) + " Positioned at: " + str(high))
                return high
            elif a[high] < x:
                a.insert(high+1, x)
                print("List a: "+ str(a) + " value: "+ str(x) +  " length array: " + str(len(a)-1) + " Positioned at: " + str(high+1))
                return high +1
            mid = mid -1
        a.insert(low, x)
        print("List a: "+ str(a) + " value: "+ str(x) +  " length array: " + str(len(a)-1) + " Positioned at: " + str(low))
        return low



def randomNumbers():
    filledList =[]
    for x in range(5):
        filledList.append(randint(50, 1400))
    newList = sorted(filledList)
    xx = randint(0, 1450)
    print("List sent: " + str(newList))
    binarysearchI(newList, xx)


while True:
    randomNumbers()




