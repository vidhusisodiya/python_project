X = dict()
n = int(input())
for i in range(n):
    key =input("enter the name")
    value = (input("enter the value")).split()
    X.update({key:value})
    marks = list(map(float,value))
    X[key] = marks
check = str(input())
av = 0
for j in X[check]:
    av = j+av
print(av/3)
