marks = int(input("Enter marks: "))
if 80 <= marks <= 100:
    print("Grade A")
elif 70 <= marks <= 79:
    print("Grade A-")
elif 60 <= marks <= 69:
    print("Grade B+")
elif 50 <= marks <= 59:
    print("Grade B")
elif 40 <= marks <= 49:
    print("Grade B-")
elif 30 <= marks <= 39:
    print("Grade C+")
elif 20 <= marks <= 29:
    print("Grade C")
elif 10 <= marks <= 19:
    print("Grade C-")
elif 1 <= marks <= 9:
    print("Bomboclaat!")
elif marks <= 0:
    print("invalid input")
