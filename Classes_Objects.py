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
