for x in range(5):
    for y in range(5):
        if x == 4 or y == 4 or x == 0 or y == 0:
            print("*", end= " ")
        else:
            print(" ", end=" ")
    print()