def fact(N):
    f = 1
    for i in range(1,N+1):
        f = f*i
    print("THE FACTORIAL OF A GIVEN NUMBER IS : " , f)

N = int(input("ENTER THE ELEMENT OF WHICH U WANT THE FACTORIAL"))
fact(N)