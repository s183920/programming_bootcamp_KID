# def add():
#     return 2
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     return a+b

def add(*args):
    return sum(args)