size = int(input("Input size of X ---> "))

for r in range(size):
    for z in range(size):
        if r + z == size-1 or r == z :
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()