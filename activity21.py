#Jeepney Simulator (interactive)
route = ["Terminal", "Perez Park", "Pacific Mall"]
passengers = ["Ana", "Ben", "Carla"]
seats = 6
fare = 13
total = 0

while True:
    print()
    print("Sakay:", passengers)
    print(len(passengers), "of", seats, "seats")
    print("1 Sakay 2 Priority seat 3 Para po!")
    print("4 Baba sa pinto 5 Baba sa harap")
    print("6 Seat check 7 Balikan 8 Exit")
    choice = input("Choice: ")

    if choice == "1":
        if len(passengers) == seats:
            print("Puno na!")
        else: 
            name = input("Name: ")
            passengers.append(name)
            total = total + fare
            print(name, "boarded at the back.")

    elif choice == "2":
        if len(passengers) == seats:
            print("Puno na!")
        else:
            name = input("name: ")
            passengers.insert(0, name)
            total = total + fare 
            print(name, "took the priority seat.")

    elif choice == "3":
        name = input("Who is getting off? ")
        if name in passengers:
            passengers.remove(name)
            print(name, "got off. Ingat! ")
        else:
            print(name, "is not on this jeep.")

    elif choice == "4":
        if len(passengers) == 0:
            print("The jeep is empty.")
        else: 
            left = passengers.pop()
            print(left, "got off at the door.")

    elif choice == "5":
        if len(passengers) == 0:
            print("The jeep is empty.")
        else: 
            front = passengers.pop(0)
            print(front, "got off at the front.")

    elif choice == "6":
        for i in range(len(passengers)):
            print("seat", i + 1, passengers[i])

    elif choice == "7":
        route.reverse()
        print("Route:", route)

    elif choice == "8":
        print("Total fare today:", total)
        break

    else:
        print("Invalid choice.")
