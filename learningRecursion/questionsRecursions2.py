# checking if a list is sorted or not
import numpy as np

list =[1.3,4,54,5,6,16,55]

def is_sorted(list, counter):
    if counter < len(list):
        return True
    if list[counter] > list[counter+1]:
        return False
    return is_sorted(list,counter+1)

def findIndexes(list, listR ,target, counter):
    if counter == len(list):
        return listR
    if list[counter] == target:
        listR.append(counter)
    return findIndexes(list, listR, target, counter+1)
"""
   we could make a helper function, to pass the parameter created
   in the function call, instead of passing them in the original
   function, or we can pass an array an update it during
   recursion
"""

"""
we need to create an object in the body of the 
function and pass it
above, the following def will contain for this case
"""
def findAllIndexes(list, target, counter):
    returnedValue = []
    if counter == len(list):
        return returnedValue
    if list[counter] == target:
        returnedValue.append(counter)
    answersFromBellow = findAllIndexes(list, target, counter+1)
    returnedValue.append(answersFromBellow)
    return returnedValue

def rotatedArray(list):
    first = list[0]
    for x in range(len(list)-1):
        list[x] = list[x+1]
    else:
        list[x+1] = first
    return list

def rotatedArrayRecursion(array):
    first = array[0]
    counter = 0
    helper(array, counter)
    array[len(array)-1] = first
    return array

def helper(list, counter):
    if counter == len(list)-1:
        return counter
    list[counter] = list[counter+1]
    helper(list, counter+1)

def rotatedBinarySearch(list, target, s, e):
    if s>e:
        return -1
    mid = s + (e-s) //2

    if list[mid] == target:
        return mid

    if list[s] <= list[mid]:#evaluate if first half is sorted
        if target >= list[s] and target<= list[mid]:#if yes, evaluate if target in this range
            return rotatedBinarySearch(list, target, s, mid-1)
        else:
            return rotatedBinarySearch(list, target, mid+1, e)

    if target >= list[mid] and target <= list[e]:
        return rotatedBinarySearch(list, target, mid+1, e)

    return rotatedBinarySearch(list, target, s, mid-1)


numArray = np.array([5, 6, 7, 8, 9, 10, 1, 2, 3])

print(rotatedBinarySearch(numArray, 3, 0, (len(numArray)-1) ))

#arrayNum = np.array([0,1,2,3,4,5])
#print(type(rotatedArrayRecursion(arrayNum)))

arrayRotated = [1,2,3,4,5]
#print(rotatedArray(arrayRotated))
#print(rotatedArray(arrayRotated))






#print(findAllIndexes([1,22,3,22,4,6], 22, 0))

#print(findIndexes([1,2,2,4,2], [], 8, 0))

#print(is_sorted(list, 0 ))
