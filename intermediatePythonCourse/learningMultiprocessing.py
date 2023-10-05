from multiprocessing import Process, Value, Array, Lock
import os
from multiprocessing import Queue
import time
from multiprocessing import Pool

#we import Value, Array for sharing data between proccesses
#becuase they don't share memory space
def add_100(number, numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        number.value +=1
        for x in range(len(numbers)):
            numbers[x]+=1
        lock.release()


if __name__ == '__main__b':
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    shared_number = Value('i', 0)
    print("Number at beginning is: ", shared_number)
    print("Array at beginning is: ", shared_array[:])

    p1 = Process(target=add_100, args=(shared_number,shared_array,lock))
    p2 = Process(target=add_100, args=(shared_number,shared_array,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('number at end is: ', shared_number)
    print("Array at the end is: ", shared_array[:])


#implementation for QUEUES
def square(numbers, queue):
    for i in numbers:
        queue.put(i+i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)

if __name__ == '__main__dd':
    numbers = range(1,6)
    q = Queue()

    p1 = Process(target= square, args=(numbers,q))
    p2 = Process(target= make_negative, args=(numbers,q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())

    #process pool can be used to manage multiple processes, a process pool object
    #controls a pool of work of proccesses to which jobs can be submited
    #split data into smaller chunks, which can then be processed by different processes
    #takes care of alot of things for you

def cube(number):
    return number * number * number

if __name__ == "__main__":

    numbers = range(10)
    pool = Pool()

    #map, apply, join, close
    result = pool.map(cube, numbers)#allocates the maximum amount of avialable procceses for this task
    #it will split that iterable into equal size chunks, and submit that into the function
    #that will be executed by multiple processors

    #pool.apply(cube, numbers[3])

    pool.close()
    pool.join()

    print(result)



