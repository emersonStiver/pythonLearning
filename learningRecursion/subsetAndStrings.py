#a new string that has removed all the a from it
from collections import deque

def removeLetter(word, letter, index, answer):
    if index == len(word):
        return answer
    if word[index] != letter:
        answer = answer + word[index]
    return removeLetter(word, letter, index+1, answer)

def skipChar(word, letter, index):
    if index == len(word):
        return ''
    if word[index] != letter:
        return word[index] + skipChar(word, letter, index + 1)
    else:
        return skipChar(word, letter, index+1)

def skipString(word, letter, index):
    if index == len(word):
        print(index)
        return ''
    if not word.startswith(letter, index):
        return word[index] + skipString(word, letter, index + 1)
    else:
        return skipString(word, letter, index+(len(letter)))

def subsets(p, up):
    if len(up) ==0:
        print(p)
        return
    ch = up[0]
    subsets(p + ch, up[1:])
    subsets(p, up[1:])

arr = []
def subsetsArray1(p, up, arr):#this one receives an array as an argument and addes the values to that array
    if len(up) ==0:
        return arr.append(p)
    ch = up[0]
    subsetsArray1(p + ch, up[1:], arr)
    subsetsArray1(p, up[1:], arr)


def subsetsArray2(p, up):#this one doesn't make use of the array argument, but it creates the array on its way back to the main function
    if len(up) ==0:
        return [p]
    ch = up[0]
    left = subsetsArray2(p + ch, up[1:])
    right = (subsetsArray2(p, up[1:]))
    """i can merge both arrays when both functions return 
    their values, and return a single array, but i want to 
    illustrate how to ask the return statement to add the 
    info from this function call so it can reach the main 
    function"""
    return left + right

def biToDe(n, e):
    if n//10 == 0:
        return n* (2**e)
    b = n%10
    return b* (2**e) + biToDe(n//10, e+1)

def sumN(num):
    counter, resultP, resultI = 1,0,0
    while counter <= num:
        if counter%2== 0:
            resultP += counter
        else:
            resultI += counter
        counter +=1
    print(f'Sum of even numbers: {resultP} and sum of odd numbers: {resultI}')



def otro(s):
    s = list(s)
    vowels = 'aeiouAEIOU'
    l, r = 0, len(s) - 1

    while (l < r):
        while (l < r and s[l] not in vowels):
            l += 1
        while (r > l and s[r] not in vowels):
            r -= 1
        s[l], s[r] = s[r], s[l]

        l += 1
        r -= 1

    return "".join(s)

print(otro('gunfire'))


def reverseVowels(s):
    deqX = deque()
    deqY = deque()
    ar = list(s)
    x = 0
    y = len(s)-1
    vowels = ['a','e', 'i', 'o', 'u', 'A','E','I', 'O','U']
    while y-x != 1 or y-x !=2:

        if ar[x] in vowels:
            deqX.append({1: [ar[x], x]})
        if ar[y] in vowels:
            deqY.append({1: [ar[y], y]})

        if len(deqY) >=1 :
            dic = deqY.popleft()
            li = dic[1]
            ar[li[1]] = li[0]
        if len(deqX) >=1:
            dic = deqX.popleft()
            li= dic[1]
            ar[li[1]] = li[0]

        x+=1
        y-=1
    print(arr)
#reverseVowels('hello')

print(0,3*10)















