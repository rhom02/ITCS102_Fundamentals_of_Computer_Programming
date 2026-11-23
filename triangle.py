

for x in range(5, 0, -1):
    for y in range(x - 1):
        print(" ", end= " ")
    for z in range(1, 6 - x + 1):
        print(z, end=" ")
    for a in range(5 - x, 0, -1):
        print(a, end=" ")
    print()