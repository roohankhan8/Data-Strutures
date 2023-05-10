def fact(x):
    a=1
    if x>0:
        while x>1:
            a*=x
            x-=1
    return a
print(fact(7))

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


print((lambda x: x**2 + 5*x + 4)(-4))


