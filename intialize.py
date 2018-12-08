# initialize __init__ chushihua

class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name, 'can walk')
        print(self.name, 'is', self.age)


# s1 = Students()
# s1.walk()
#
# s2 = Students()
# s2.walk()

s1 = Students("Jason", "18")
s1.walk()

s2 = Students("James", "15")
s2.walk()