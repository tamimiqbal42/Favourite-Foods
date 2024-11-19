nam = input("Please inter your name: ")
name = nam.upper()
age = int(input("Please inter your age: "))


if age>=18:
    if age >= 20:
        premission = True
        print(f"Permission granted, {name}. You are allowed to enter the club.")
    else: 
        print(f"Dear perticepant {name}, your age :{age} . You need permission first for inter the club.")
    
else:
    print(f"Sorry, {name}. You are not allowed to enter the club.")