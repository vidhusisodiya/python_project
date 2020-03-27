N = int(input("ENTER THE ELEMENT TO BE CHECKED \n"))
i = 2
FLAG = 1
for i in range(2,N):
    if N % i == 0:
        FLAG+=1

if FLAG == 1:
    print("THE GIVEN NUMBER IS A PRIME NUMBER")
else:
    print("THE GIVEN NUMBER IS NOT A PRIME NUMBER")



