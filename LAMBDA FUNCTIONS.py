from functools import reduce

S = lambda a : a*a
z = S(5)
print(z)
lst = []
N = int(input("ENTER THE LIMIT OF THE LIST"))
for i in range(N):
    e  = int(input("enter the element"))
    lst.append(e)
print(lst)

m = lambda n: n%2 == 0
even = list(filter( m , lst))
print(even)
double = list(map(lambda r : r*r , lst))
print(double)
sum = reduce(lambda a,b: a+b,lst)
print(sum)