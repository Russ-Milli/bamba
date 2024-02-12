def is_palindrome():
    word = input("Enter a word:")

    if word == word[::-1]:
        print("The word is palindrome")
    else:
        print("The word is not palindrome")


is_palindrome()




def is_palindrome2():
    num1 = (input("Enter a number:"))

    if num1 != num1[::-1]:

        print("The number is not palindrome")
    else:
        print("The number is palindrome")


is_palindrome2()
