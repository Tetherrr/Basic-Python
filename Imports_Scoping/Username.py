class User:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def call(self):
        print(f"User: {self.n}, {self.a}")

