from array import *

arr = array('i' , [])
N = int(input("ENTER THE LIMIT OF THE ARRAY \n"))
for i in range(N):
    Z = int(input("ENTER THE elements OF THE ARRAY \n"))
    arr.append(Z)
for E in arr:
    print("THE GIVEN ELEMENT OF ARRAY IS : " , E)
c = 0
M = int(input("ENTER THE ELEMENT TO BE SEARCHED"))
for e in arr:
    if e == M:
        print("THE ELEMENT IS FOUND AT INDEX " , c+1)
        break
    c+=1
else:
    print("GIVEN ELEMENT IS NOT FOUND IN ARRAY")

print("GIVEN ELEMENT IS NOT FOUND IN ARRAY" , arr.index(M))

print(arr.sort())