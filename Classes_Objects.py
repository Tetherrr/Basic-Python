# class Character:
#     name = "Name"
#     hp = 100
#     mp = 50
#     atk = 10
#     lvl = 1

class Character:
    def __init__(self, name, hp, mp, atk, lvl):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.level = lvl


c1 = Character("MAx", 100, 200, 150, 50)
c1.name = "Mox"
c1.atk = 200
c1.lvl = 10

print(c1.name)


# class Product:
#     Name = "Eyeglass"
#     Product_Number = 220210
#     Price = 1500

# Organized Structure of creating object
class Product:
    def __init__(self, name, product_number, price):
        self.name = name
        self.product_number = product_number
        self.price= price


p1 = Product("Glass", 202021, 1200)
print(p1.name, p1.product_number, p1.price)

class User:
    def __init__(self, firstName, lastName, likesCount, friendsName):
        self.fn = firstName
        self.ln = lastName
        self.lc = likesCount
        self.fl = friendsName

    def introduction(self):
        print( "User Info: "+ self.fn, self.ln + " Likes:", self.lc)

        print("Friend List: ")
        for friend in self.fl:
            print("- ", friend)

userOne = User("Moises", "Paule", 100, ["Paul", "Mark", "Ric"])
print(userOne.introduction())

class employee:
    def __init__(self, name, age, wage):
        self.name = name
        self.age = age
        self.wage = wage

    def employeeInfo(self):
        print("Name:", self.name, "Age:",self.age,)
        print("Wage:", self.wage)

print("Enter Employee Name, Age and Wage: [Provided with space]")

inputName = str(input("Enter Name: "))
inputAge = int(input("Enter Age: "))
inputWage = float(input("Enter Wage: "))


EmployeeOne = employee(inputName, inputAge, inputWage)
EmployeeOne.employeeInfo()
