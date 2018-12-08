# inheritance yichan

class Father:
    name = "Jason"
    def eat(self):
        print("I can eat")

class Mother:
    def walk(self):
        print('walk like mother')

class Son(Father,Mother):  # inheritance class Father/Mother
    def eat(self):
        print("eat like son") # overriden
    def walk(self):
        print("walk like son")

littleJason = Son()
littleJason.walk()
# by Jason