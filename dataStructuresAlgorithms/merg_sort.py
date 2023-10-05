
def merge_sort(list):
    """Sorts a list in ascending order
       returns a new sorted list

    Divide: find the mid point of the list and divde into sublist
    Conquer: recursively sort the sublists created in previous step
    Combine: merge the sorted sublists created in previous step"""

    if len(list) <= 1:
        return list
    #DIVIDE
    left_half, right_half = split(list)

    #conquer
    left = merge_sort(left_half)  #[56,33,59,50, 40,10, 37]
    right = merge_sort(right_half)

    #It gets combined
    return merge(left, right)

def split(list):
    """divde the unsorted list at midpoint into sublists
    returns two sublists - left and right"""
    mid_point = len(list) //2
    left, right = list[:mid_point], list[mid_point:]
    print(left)
    print(right)
    return left, right

def merge(left, right):
    """merges two lists(arrays), sorting them in the process
    returns a newm merged list"""
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j+=1
    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1
    return l

my_list = [56,33,59,50, 40,10, 37]
l = merge_sort(my_list)
print(l)