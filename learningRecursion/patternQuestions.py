def triangle(rows:int, colums:int):
    if rows == 0:
        return #base condition
    if colums < rows:
        print('*', end=' ')
        triangle(rows, colums+1)
    else:
        print()
        triangle(rows-1, 0)
    print("done")
#triangle(4,0)


def bubble_sort(list, i, repeat):
    if repeat == 0:
        return
    if i+1 < len(list):
        first = list[i]
        if list[i] > list[i+1]:
            list[i] = list[i+1]
            list[i+1] = first
        bubble_sort(list, i+1, repeat)
    else:
        bubble_sort(list, 0, repeat-1)

def selection_sort(list,repeat, i, j, li ):#mine selects the least argument
    if repeat == 0:
        return
    if j < len(list):
        if list[li] > list[j]:
            li = j
        selection_sort(list, repeat, i, j+1, li)
    else:
        stored = list[i]
        list[i], list[li] = list[li], stored
        selection_sort(list, repeat-1, i+1, i+1, i+1)

def selection_sortKunal(arr, r, c, max):#his selects the largest argument
    if r == 0:
        return
    if c < r:
        if arr[c] > arr[max]:
            selection_sortKunal(arr, r, c+1, c)
        else:
            selection_sortKunal(arr, r, c+1, max)
    else:
        temp = arr[max]
        arr[max] = arr[r-1]
        arr[r-1] = temp
        selection_sortKunal(arr, r-1, 0, 0)

    """Merge sort"""

def merge_sort(list):
    if len(list)==1:
        return list
    mid = len(list) //2
    left_half, right_half = list[:mid], list[mid:]

    left = merge_sort(left_half )
    right = merge_sort(right_half)

    sortedList = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            sortedList.append(left[l])
            l +=1
        else:
            sortedList.append(right[r])
            r+=1
    while l < len(left):
        sortedList.append(left[l])
        l +=1
    while r < len(right):
        sortedList.append(right[r])
        r +=1
    return sortedList





def merge_sort_inplace(list, s , e):
    if e-s==1:
        return
    mid = (s+e)//2

    merge_sort_inplace(list, s, mid)
    merge_sort_inplace(list, mid, e)

    mergeInPlace(list, s, mid, e)

def mergeInPlace(list, s, m, e): #[48,52,38,39,45]
    mix = []
    i = s
    j = m
    while i < m and j < e:
        if list[i] < list[j]:
            mix.append(list[i])
            i=i+1
        else:
            mix.append((list[j]))
            j=j+1
        while i < m:
            mix.append(list[i])
            i+=1
        while j < e:
            mix.append((list[j]))
            j+=1
        for l in range(len(mix)):
            list[s+l] = mix[l]



exampleArray =[48,52,38,39,45]
myarray = [64,25,12,22,11,34,12,4,4,66,3,1]
myarray2 = [64,25,12,22,11,34,12,4,4,66,3,1]

merge_sort_inplace(exampleArray, 0, len(exampleArray)-1)
print(exampleArray)
#selection_sortKunal(myarray, len(myarray), 0, 0)
#selection_sort(myarray2, len(myarray2)-1,  0, 1, 0)
#print(myarray)
#print(myarray2)

#bubble_sort(myarray,0, (len(myarray)-1))
