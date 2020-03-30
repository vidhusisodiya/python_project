from numpy import *
a = zeros((3,3 ),int )
m = int(input("enter the number of rows"))
n = int(input("enter the number of columns"))
a = zeros((m,n), int)
for i in range(len(a)):
    for j in range(len(a[i])):
        x = int(input("enter the elemnents"))
        a[i][j] = x
print(a)
print(transpose(a))
print(a.flatten())