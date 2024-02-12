num = int(input("Enter number: "))

if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

    age = int(input("Enter your age: "))

    if 18 <= age <= 100:
        print(f"{age} is eligible to vote")
    else:
        print(f"{age} is not eligible to vote")

    age = int(input("Enter your age: "))

    if age >= 18:
        print(f"{age} Can access GTA online")
    else:
        print(f"{age} Can not access GTA online")
