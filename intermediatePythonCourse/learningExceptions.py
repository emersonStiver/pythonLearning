class valueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
def test_value(x):
    if x < 100:
        raise valueTooSmallError("Too small number", x)

try:
    test_value(90)
except ZeroDivisionError as e:
    print("not possible to divide by 0")
except valueTooSmallError as e:
    print(e)
else:#this is executed if no excepts are raised
    print("everything is find")


finally:#executed no matter what
    #runs no matter what,
    print("cleaning up....")