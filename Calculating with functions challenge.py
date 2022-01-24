def zero():
    global a, b
    a, b = 0, 0


def one():
    global a, b
    a, b = 1, 1
    def plus():
        return a + b


def two():
    global a, b
    a, b = 2, 2


def three():
    global a, b
    a, b = 3, 3


def four():
    global a, b
    a, b = 4, 4


def five():
    global a, b
    a, b = 5, 5


def six():
    global a, b
    a, b = 6, 6


def seven():
    global a, b
    a, b = 7, 7


def eight():
    global a, b
    a, b = 8, 8


def nine():
    global a, b
    a, b = 9, 9


def plus(func):
    a = 0

    def inner():
        func(*args)
        a += b

    return inner


def minus():
    return a - b


def times():
    return a * b


def divided_by():
    return a // b


one(plus(two()))
two(minus(three()))


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


@star
@percent
def printer():
    print("Hello buddy")


star(percent(printer()))
