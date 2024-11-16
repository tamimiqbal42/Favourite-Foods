favourite_foods = [] # initialize empty list for favourite foods
while True:
    print("Favourite Foods Manager")
    print("0. Exit")
    print("1. Add foods")
    print("2. Remove foods")
    print("3. View favourite all foods")
    
    choice = input("Choose an option: ") # From taken user input
    
    if choice == "0":
        print("Thanks for using Favourite Foods Manager")
        break
    elif choice == "1":
        food = input("Enter you favourite food name: ")
        favourite_foods.append(food)
        print(f"{food} added Successfully")

    elif choice == "2":
        food = input("Enter a food name which you want to remove: ")
        favourite_foods.remove(food)
        print(f"{food} remove Successfully")
    elif choice == "3":
        if favourite_foods:
            print("Your favourite foods: ")
            for index, food in enumerate(favourite_foods, start=1):
                print(f"{index}.{food}")
        else:
            print("Food List is empty or didn't added yet! ")
            
    else:
        print("Invalid Choice!")