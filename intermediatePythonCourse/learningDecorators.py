#Decorators, difference betweenfunction and class decorators
import functools


# it adds new functionality to a new function

#THIS IS THE FIRST WAY TO CREATE A DECORATOR
def start_end_decorator(func):
    def wrapper():
        #i can do something before
        print("start")
        func()
        #i can do something after
        print("end")
    return wrapper
def print_name():
    print("Alex")

#print_name = start_end_decorator(print_name)
#print_name()

#THIS IS THE SECOND WAY TO CREATE A DECORATOR

def start_end_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):#this sintax allows me to use as many arguments and keywords arguemtns as i want
        #i can do something before
        #we can access the values passed to wrapper

        argsArgument = args[0]
        print(argsArgument)

        typo = args[1]
        print(typo)

        typ2 = args[2]
        print(typ2)

        print("start")
        result = func(*args, **kwargs)
        #i can do something after
        print("end")
        return result +10 +123123123
    return wrapper
@start_end_decorator2
def add5(x, tipo= 5, oper=""):
    print("hola soy add5")
    return x +5

#result = add5(10, 4, "multiplication")
#print(result)
#if we want the main function to have arguments, we also need to specify those arguments or keywords in our wrapper
#this is how we can extend the behaviour of a function with a decorator

#function identity, we need to tell the interpreter that the function we are using is
#add5 not wrapper, we can fix that by importing functools




#DECORATORS FOR REPETITIONS
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat



@repeat(num_times=3)
def greet(name):
    print(f'hello{name}')

#greet("alex")





#NESTED DECORATORS

def decorator2(func):
    @functools.wraps(func)
    def wrapper (*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]

        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

def decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper

#they will be executed in the order they are listed

@decorator2
@decorator1
def say_hello(name):
    greeting = f'hello{name}'
    print(greeting)
    return greeting

#say_hello("emer")




#CLASS DECORATOR
#class d do the same thing as class decorator, but they are used to maintain and update a state
#in this example i want to keep track how many times i've executed this function

class Countcalls:
    def __init__(self, func):
        self.func = func
        self. num_calls = 0
    def __call__(self,*args,**kwargs):
        self.num_calls += 1
        print(f'this is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@Countcalls
def saludar(x):
    print("Hello: " + str(x))

saludar("emer")
saludar("danna")
