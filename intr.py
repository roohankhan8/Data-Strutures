#Factorial
def fact(x):
    a=1
    if x>0:
        while x>1:
            a*=x
            x-=1
    return a
#print(fact(7))
#OR
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
# print(factorial(6))

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
# quad(0,25,0)

#lambdas
# print((lambda x: x**2 + 5*x + 4)(-4))

#map
nums=[1,2,3,4,5]
res=list(map(lambda x: x+5,nums))
# print(res)

#filter
res2=list(filter(lambda x: x%3==0, nums))
# print(res2)

#generators
def count():
    i=2
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
# decorated()
#OR
@decor
def hello():
    print('Hello World')
# hello()

#Recursion
def is_even(x):
    if x==0:
        return True
    else:
        return is_odd(x-1)
def is_odd(x):
    return not is_even(x)
# print(is_even(99), is_odd(77))

def fib(x):
    if x==0 or x==1:
        return 1
    else: 
        return fib(x-1) + fib(x-2)
# print(fib(4))

#args and kwargs
def func(nargs, *args, **kwargs):
    print(nargs, args, kwargs)
# func(1,2,3,4,5,6, a=7, b=8)

def func(**kwargs):
    print(kwargs['zero'])
# func(a=0, zero=8)

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
# print(felix.color)

#inheritance
#superclass, subclass inherits from it
class Animal:
    def __init__(self, name, color):
        self.name=name
        self.color=color
    def me(self):
        print("I'm an animal")
class Cat(Animal):
    def purr(self):
        print('Purrr')

class Dog(Animal):
    def bark(self):
        print('Woof')
        super().me()
fido=Dog('Fido', 'brown')
# print(fido.color)
# fido.bark()

#magic methods also dunders
#double underscores at start and end
#common use = operator overloading
class Vector2D:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
first=Vector2D(5, 7)
second=Vector2D(3, 9)
result=first+second
# print(result.x)
# print(result.y)
'''
__sub__ -
__mul__ *
__truediv__ /
__floordiv__ //
__mod__ %
__pow__ **
__and__ &
__xor__ ^
__or__ |
__lt__ <
__le__ <=
__eq__ ==
__ne__ !=
__gt__ >
__ge__ >=
__len__
__getitem__
__setitem__
__delitem__
__iter__
__contains__
'''

class SpecialString:
    def __init__(self, cont):
        self.cont=cont
    def __truediv__(self, other):
        line = "="*len(other.cont)
        return "\n".join([self.cont, line, other.cont])
spam=SpecialString('spam')
hello=SpecialString('Hello there')
bye=SpecialString('Byebye')
# print(spam/hello)
# print(hello/bye)
'''
first arg become self.cont and second arg becomes other.cont
here, other = Hello there
self.cont = spam
other.cont = Hello there
truediv func returns each cont with a line break and a line b/w them
'''

class SpecialString1:
    def __init__(self, cont):
        self.cont=cont
    def __gt__(self, other):
        for i in range(len(other.cont)+1):
            result=other.cont[:i]+'>'+self.cont
            result+='>'+other.cont[i:]
            print(result)
        print(self.cont)
        print(other.cont)
roohan, khan=SpecialString1('Roohan'), SpecialString1('Khan')
# khan>roohan

'''
encapsulation = packaging of funcs and vars in object
Data hiding = implementation details should be hidden
weakly private methods have one underscores at beg
strongly private methods have double underscores at beg
'''
#weakly
class Queue:
    def __init__(self, cont):
        self._hiddenlist=list(cont)
    def enqueue(self, value):
        self._hiddenlist.insert(0,value)
    def dequeue(self):
        self._hiddenlist.pop(-1)
    def __repr__(self):
        return 'Queue({})'.format(self._hiddenlist)
q=Queue([1,2,3])
# print(q)
# q.enqueue(0)
# print(q)
# q.dequeue()
# print(q)
# print(q._hiddenlist)

#strongly
class Spam:
    __egg=7
    def print_egg(self):
        print(self.__egg)
s=Spam()
# s.print_egg()
# print(s._Spam__egg)
# print(s.__egg)

'''
class methods are called on class
static methods

property are used to make attribute read only
setter getter func
setter gets prop val
getter gets val
'''
#classmethod
class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def cal_area(self):
        return self.width*self.height
    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)
# square=Rectangle.new_square(5)
# print(square.cal_area())
'''
new_square is a class method called on class
'''
#staticmethod
# class Pizza:
#     def __init__(self, toppings):
#         self.toppings=toppings
#         self._pine_all=False
#     @staticmethod
#     def val_top(topping):
#         if topping=='pineapple':
#             raise ValueError('No pineapples')
#         else:
#             return True
#     @property
#     def pine_all(self):
#         return self._pine_all
#     @pine_all.setter
#     def pine_all(self, val):
#         if val:
#             password=input('Enter the password: ')
#             if password=='roohan':
#                 self.pine_all=val
#             else:
#                 raise ValueError('Alert!')
# # ingredients=['cheese','onions','spam']
# pizza=Pizza(['cheese','tomato'])
# print(pizza.pine_all)
# pizza.pine_all=True
# print(pizza.pine_all)
# # if all(Pizza.val_top(i) for i in ingredients):
# #     pizza=Pizza(ingredients)

class Pizza:
    def __init__(self, toppings):
        self.toppings=toppings
        self._pine_all=False
    @property
    def pine_all(self):
        return self._pine_all
    @pine_all.setter
    def pine_all(self, val):
        if val:
            password=input('Enter the password: ')
            if password=='roohan':
                self._pine_all=val
            else:
                raise ValueError('Alert!')
# pizza=Pizza(['cheese','tomatoes'])
# print(pizza.pine_all)
# pizza.pine_all=True
# print(pizza.pine_all)

try:
    num1=1
    num2=0
    print(num1/num2)
except:
    print('Error')
finally:
    print('anyway')
# OR
# else:
#     print(4)
