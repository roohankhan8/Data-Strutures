#Factorial
def fact(x):
    a=1
    if x>0:
        while x>1:
            a*=x
            x-=1
    return a
print(fact(7))
#OR
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial(6))

#Quadratic Equations
def quad(a,b,c):
    d=b**2 - 4*a*c
    if d>0:
        if type(d**0.5)==type(2):
            print('Rational and unequal')
        else:
            print('Real and unequal')
    else:
        print('Imaginary and unequal')
quad(0,25,0)

#lambdas
print((lambda x: x**2 + 5*x + 4)(-4))

#map
nums=[1,2,3,4,5]
res=list(map(lambda x: x+5,nums))
print(res)

#filter
res2=list(filter(lambda x: x%3==0, nums))
print(res2)

#generators
def count():
    i=10
    while i>0:
        yield i
        i-=1
for i in count():
    print(i)

#decorators
def decor(func):
    def wrap():
        print('==========')
        func()
        print('==========')
    return wrap
def hello():
    print('Hello World')

decorated=decor(hello)
decorated()
#OR
@decor
def hello():
    print('Hello World')
hello()

#Recursion
def is_even(x):
    if x==0:
        return True
    else:
        return is_odd(x-1)
def is_odd(x):
    return not is_even(x)
print(is_even(99), is_odd(77))

def fib(x):
    if x==0 or x==1:
        return 1
    else: 
        return fib(x-1) + fib(x-2)
print(fib(4))

#args and kwargs
def func(nargs, *args, **kwargs):
    print(nargs, args, kwargs)
func(1,2,3,4,5,6, a=7, b=8)

def func(**kwargs):
    print(kwargs['zero'])
func(a=0, zero=8)

#OOP
'''
objects are made using classes
classes are blueprints
class methods = funcs in classes
'''
class Cat:
    def __init__(self, color, legs):
        self.color=color
        self.legs=legs
felix=Cat('black', 4)
rover=Cat('white', 3)

print(felix.color)



