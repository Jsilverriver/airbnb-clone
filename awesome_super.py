class Dog:
    def __init__(self):
        print("Dog class f init")

    def pee(self):
        print("Dog class f pee")


class Puppy(Dog):
    def __init__(self):
        print("Puppy class f init")
        super().__init__()


p = Puppy()

