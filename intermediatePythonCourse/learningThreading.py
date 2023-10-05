from threading import Thread, Lock, current_thread
from queue import Queue
import time


database_value = 0
#erase condition happens when 2 threads try to modify one variable at the same time

def increase(lock):
    global database_value
    lock.acquire()
    local_copy = database_value
    #processing....
    local_copy +=1
    time.sleep(0.1)
    database_value = local_copy
    lock.release()

if __name__ == "__main__k":
    lock = Lock()
    print('start value', database_value)
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)
    print('end main')

#threads live  in the same memory space, it makes exchanging data very easily


def worker(q,lock):
    while True:
        with lock:
            value = q.get()
        #processing

            print(f'in {current_thread().name} got {value}')
        q.task_done()


if __name__ == "__main__":
    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):

        thread = Thread(target=worker, args=(q,lock))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)
    q.join()


    #q.put(1)
    #q.put(2)
    #q.put(3)
    # 3 2 1 --->

    #first = q.get()#removes first item
    #q.empty()#returns true if queue is empty
    #q.task_done()#tells the program that we are done with processing
    #whenever we remove an item from the list
    #q.join()#blocks until all items in the queue have been processed

    print('end main')



