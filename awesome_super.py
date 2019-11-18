class Dog:
    def __init__(self):
        print("Dog class f init")

    def pee(self):
        print("Dog class f pee")


class Puppy(Dog):
    def pee(self):
        print("Puppy class f pee")
        super().pee()


p = Puppy()
p.pee()

