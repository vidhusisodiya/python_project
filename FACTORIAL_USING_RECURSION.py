def fact(N):
    if N ==0:
        return 1
    Z = N * fact(N-1)
    return Z
N = int(input("ENTER THE NUMBER"))
result = fact(N)
print(result)