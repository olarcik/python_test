def outer():

    def inner():
        result = 2 + 5
        return result

    return inner

inner_function = outer()
print(inner_function())


def func1(give_me_a_function):
    print('before')
    give_me_a_function()
    print('after')

def simple1():
    print('simple1')

def simple2():
    print('simple2')

func1(simple1)
func1(simple2)

#Decorator
print('Decorator')
def add_text(func):

    def wrapper():
        print('before')
        func()
        print('after')

    return wrapper


def simple1():
    print('simple1')

simple1()

simple1 = add_text(simple1)

simple1()

def simple2():
    print('simple2')

simple2()

simple2 = add_text(simple2)

simple2()

#Good decorator
print('Good decorator')
#Decorator
print('Decorator')
def add_text(func):

    def wrapper():
        print('before')
        func()
        print('after')

    return wrapper

@add_text
def simple1():
    print('simple1')

@add_text
def simple2():
    print('simple2')

simple1()
simple2()

#Complex example
print('Complex example')
def add_logs(func):

    def wrapper(*args):
        print(f'function {func.__name__} started')
        result = func(*args)
        print(f'finished {func.__name__}')
        return result

    return wrapper

@add_logs
def calc(x):
    print(x*2)

@add_logs
def calc2(x, y):
    print(x * x)

@add_logs
def simple1():
    print('simple1')

simple1()
calc(3)
calc2(3,7)

