def script():

    print ("1 - atņemšana")
    print ("2 - saskaitīšana")
    print ("3 - reizināšana")
    print ("4 - dalīšana")

    choice = input ("Izvēlies no 1-4 : ")

    num1 = float(input ("Izvēlies 1. ciparu - "))
    num2 = float(input ("Izvēlies 2. ciparu - "))

    if choice == "1":
        print (f"{num1} - {num2} = {num1-num2}")
    elif choice == "2":
        print (f"{num1} + {num2} = {num1+num2}")
    elif choice == "3":
        print (f"{num1} * {num2} = {num1*num2}")
    elif choice == "4":
        print (f"{num1} : {num2} = {num1/num2}")

    restart = input("Would you like to use calculator again? ")
    if restart == "yes" or restart == "y":
        script()
    elif restart == "n" or restart == "no":
        print("Good bye!")
script()
