# Single inheritance
class Parent:
    def function1(self):
        print("Function of Parent")

class Child(Parent):
    def function2(self):
        print("Function of Child")

# Multiple inheritance
class Mother:
    def mother(self):
        print("Mother's feature")

class Father:
    def father(self):
        print("Father's feature")

class Child(Mother, Father):
    def child(self):
        print("Child's feature")

# Multilevel inheritance
class Grandfather:
    def grandfather(self):
        print("Grandfather's feature")

class Father(Grandfather):
    def father(self):
        print("Father's feature")

class Child(Father):
    def child(self):
        print("Child's feature")
