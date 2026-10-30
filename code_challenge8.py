rows = int(input("Enter the number of rows: "))

for r in range(0, rows):
    for n in range(0, rows - r - 1):
        print(" ", end=" ")
    for n in range(0, r + 1):
        print("*", end= " ")
    print()
    
for r in range(0, rows - 1):
    for n in range(0, r + 1):
        print(" ", end=" ")
    for n in range(0, rows - r - 1):
        print(" ", end=" ")
    print()        