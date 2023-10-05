
class NumbersExample:
#
    def imprimir(self, n):
        print(n)
        n+=1
        if n <= 5:
            self.imprimir(n)
        print("done")

    def fibo(self,n):
        #base condition
        if n<2:
            return n
        return self.fibo(n-1) + self.fibo(n-2)

    def binary_search(self, my_list, target, start, end):
        #print(f'start: {start}  end: {end}')
        if start> end:
            return -1
        mid = (start+end)//2
        if start >= end:
            return -1

        if my_list[mid] == target:
            return mid
        if target > my_list[mid]:
            return self.binary_search(my_list, target, mid+1, end)
        else:
            return self.binary_search(my_list, target, start, mid-1)

    def sumArrays(self, list):
        if len(list)<1:
            return
        i = 0
        new_list = []
        while i < (len(list)-1):
            new_list.append( list[i] + list[i+1] )
            i+=1
        self.sumArrays(new_list)
        print(list)
num = NumbersExample()

arr = [ 1,2,3,4,5]
num.sumArrays(arr)





#num.imprimir(1)
#print(num.fibo(50))
#my_list = [2,4,7,9,12,14,23,46,338 ]
#print(num.binary_search(my_list, 4, 0, len(my_list)))





