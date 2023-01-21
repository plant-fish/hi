matrix = [[1,2,3],[4,5,6]]
for i in matrix:
    for j in i:
        print(j, end=' ')
    print()
print()

for i in matrix:
    for j in i:
        print(j,end='')
    print()
print()
    
print(matrix[0])
print()

matrix[1][0]
matrix2=matrix[::-1]
print(matrix2)
print()

print(len(matrix))
print(len(matrix[0]))
print()

i=0
z=0
y=0
k = []
b = []
while i<len(matrix):
    j=len(matrix[0])-1
    while j>=0:
        print(matrix[i][j])
        b.append(matrix[i][j])
        j=j-1
        z=z+1
    i=i+1
    k.append(b)
    b = []

print(k)
print()

x = 'FishC'
y = 'FishC'
print(x is y)

x = [1,2,3]
y = [1,2,3]
print(x is y)

A = [None]*3
for i in range(3):
    A[i] = [None]*2
print(A)
print()
        
    
x = [1,2,3]
y = x
x[1] = 1
print(x)
print(y)
print()

x = [1,2,3]
y = x.copy()
x[1] = 1
print(x)
print(y)
print()

x = [1,2,3]
y = x[:]
x[1] = 0
print(x)
print(y)
print()

import copy
x = [[1,2,3],[4,5,6]]
y=copy.deepcopy(x)
x[1][1]=0
print(x)
print(y)
print()

oho = [1,2,3,4,5]
oho = [i * 2 + 1 for i in oho]
print(oho)
print()

col2=[row[1] for row in matrix]
print(col2)
print()

diag = [matrix[i][i] for i in range(len(matrix))]
print(diag)
print()

t = range(len(matrix))
diag2 = [matrix[i][i] for i in t[::-1]]
print(diag2)
print()

##二位列表-》一位列表
flatten = [col for row in matrix for col in row]
print(flatten)
print()

flatten = []
for row in matrix:
    for col in row:
       flatten.append(col)
print(flatten)
print()

a1, a2, *a3 = "FishC"
print(a1)
print(a2)
print(a3)
print()

aa=[1,2,3]
bb = [4,5,6]
cc=(aa,bb)
print(cc)
cc[0][0]=0
print(cc)
print()

