#boolean variable
tuloy = True

while tuloy == True:
    ask = input("Do you wish to continue this program (yes / no) --> ")

    if ask.lower() == "yes":
        print("continuing ")
        continue
    else: 
        print("stopping now")
        break