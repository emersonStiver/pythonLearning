#great tool for research management, allocate and release resources
from threading import Lock
from contextlib import contextmanager
#with open('notes.txt', 'w') as file:#with a context manager
    #file.write('some todo')

file = open('notes.txt', 'w')#same thing without a contesxt manager
#try:
   # file.write('some todo')
#finally:
    #file.close()

lock = Lock()
lock.acquire()

lock.release()

with lock:
    pass
    #......




class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("enter")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception han been handled')
        #print('exc: ' ,exc_type, exc_value)
        print("exit ")
        return True

with ManagedFile('notes.txt') as file:
    print('do some stuff')
    file.write('some todo')
    dosomething()
print("continuing")

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()
with open_managed_file('notes2.txt') as f:
    f.write('some todoo...')







