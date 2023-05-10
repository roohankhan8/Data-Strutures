import numpy as np

'''
all elements of same types in array
n dimensional array
dimesnions=axes
no of axes = rank

ndim=rank
shape=order of matrix
size
'''

b = np.array([1,2,3,4])
print(b[0])

'''
ones(row,column)
zeros(row,column)
random.random(no. of ele)
full((row, col), val)
empty(row,column)
eye
identity
copy
loadtxt
save
'''
a=np.ones((3,2))
print(a)

'''
arrange(start, end, step)
linspace(start, end, no of ele)
'''
print(np.linspace(0,20, 14))

'''
reshape (gives new array)
resize (modifies)
ravel (flatens)
transpose
'''
x=np.array([[1,2,3],[4,5,6]])
print(x.reshape(3,2))

'''
slicing star:stop:step
b[0:2,1] second ele of first 2 rows in mdarray
b[...,2] third ele of every row

add
remainder
dot
exp
sqrt
around
trunc
floor
ceil
log
sum
min
max
cumsum
mean
median
axis = 1 row
axis = 0 columnn
corrcoef
std
broadcasting = operations of same order arrays
'''

A=[[1,2],[3,4],[5,6]]
T=[[0,0,0],[0,0,0]]
print(A)
for k in range(len(A)):
    for j in range(len(A[0])):
        T[j][k]=A[k][j]
for r in T:
    print(r)




