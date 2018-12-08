# object oriented 3

class Student:
    name = 'Jason'
    age = 25 # class variable

    def eat(self):
        print(self.name,'can eat'+' and he is ',self.age)

    @staticmethod
    def walk():
        print("student can walk")


student = Student()
student.eat()
student.walk()

student2=Student()
student2.walk()
student2.eat()