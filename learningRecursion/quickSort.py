

def sort(list, low, high):
    if low >= high:
        return
    s = low
    e = high
    m = s + (e-s) //2
    pivot = list[m]

    while s<=e:

        #also a reason why if its already sorted,it will not swap
        while list[s] < pivot:
            s+=1
        while list[e] > pivot:#if it enters if the value is on the right position before or after the pivot
            e-=1
        if s<=e:
            temp = list[s]
            list[s] = list[e]
            list[e] = temp
            s+=1
            e-=1
    sort(list, low, e)
    sort(list, s, high)

#arr = [5,4,3,2,1,5]
arr = [5,6,3,2,3,6,2,21,5,7,3,4]
sort(arr, 0, len(arr)-1)
print(arr)
