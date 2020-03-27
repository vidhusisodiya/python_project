N = int(input("ENTER THE ELEMENT TO BE CHECKED"))
for i in range(2,N):
    if N % i == 0:
        print("THE GIVEN NUMBER IS A PRIME NUMBER")
        break
else:
    print("NOT A PRIME NUMBER")