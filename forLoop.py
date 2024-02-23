fruits = ["Apple", "Banana", "Orange", "Pears"]
Basket = tuple(fruits)
Basket = fruits.copy()
print(fruits)

for fruit in fruits:
    print(str(fruit))

else:
    print("All Fruits Printed")


for y in range(10):
    print("Hello")

username = ["Moon", "Sun", "Pluto"]
password = ["abc123", "123abc", "aaa"]

userInput = str(input("Enter Username: "))
passInput = str(input("Enter Password: "))


print(" ")

for x in  range(len(username)):
    if userInput == username[x]:
        print("Username Found!")

    else:
        print("Username not found! ")
        break

    if userInput == username[x] and passInput == password[x]:
        print("Log in successful")
        break
    else:
        print("Error")
        break

else:
    print("Program End")

