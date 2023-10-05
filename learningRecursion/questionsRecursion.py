class questions:
    def __init__(self):
        self.sum = 0

    def printReverse(self, n):
        if n == 0:
            return
        print(n)
        self.fun(n-1)
        print(n)

    def factorial(self, n):
        if n <= 1:
            return n
        return n * self.factorial(n-1)

    def sum_of_digits(self, list1, counter):
        if counter == (len(list1)-1):
            return list1[counter]
        return list1[counter] + self.sum_of_digits(list1, counter+1)
    def reverseNumbers(self,n):# 2 3 4
        if n//10 ==0:
            print(int(n))
            return
        print(int(n%10), end= " ")
        self.reverseNumbers(n//10)
    #reverse an array of numbers
    def reverseArray(a):
        endP = (len(a) - 1)
        for x in range(len(a) // 2):
            print(x)
            a[x], a[endP] = a[endP], a[x]
            endP -= 1
        print(a)

    def reverseSumPlaceValue(self,n, base):# 2 3 4
        if n//10 == 0:
            return n
        base = base - 1
        return ((n%10) *10**base) + self.reverseSumPlaceValue(n//10, base)

    def count_occurances(self, n, counter=0):
        if n<=9:
            if n==0: return counter+1
            else:    return counter

        if n%10 ==0:
            counter +=1
        return counter + self.count_occurances(n//10)

q = questions()
#print(q.count_occurances(12312393203043040030320302302030003003030))
#print(q.reverseSumPlaceValue(123454, 6))
#print(((4%10) * 10**2) +23)
#q.reverseNumbers2(231)
#print(q.sum_of_digits([1,3,4,9],0))
#q.printReverse(5)
#print(q.factorial(10))







