#Small function that can hold many args looks more efficient than creating functions
add = lambda x,y,z : x + y + z
print(add(2,3,3))

multiply = lambda x,y : x * y
print(multiply(2, 5))


while True:
    number = int(input("Enter Num: "))  # Using a descriptive variable name
    triple = lambda x: x * 3  # Simplified lambda expression
    print(triple(number))

    print(" ")

    choice = input("Y/N? ").upper()  # Using a descriptive variable name and storing input directly in uppercase

    if choice == "Y":
        print("Continue")
    elif choice == "N":
        break

