def fibo(N):
    a = 0
    b = 1
    print(a , " , ", b , end=" , ")
    for i in range(2,N):

        c = a+b
        print(c , end=" , ")
        a = b
        b = c

N = int(input("ENTER THE LIMIT OF THE SERIES"))
fibo(N)