

# !multiple inheritance syntax
# A class can be derived from more than one superclass in Python. This is called multiple inheritance.

class SuperClass1:
    # features of SuperClass1
    pass

class SuperClass2:
    # features of SuperClass2
    pass

class MultiDerived(SuperClass1, SuperClass2):
    # features of SuperClass1 + SuperClass2 + MultiDerived class
    pass

# !e.g.,

class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")


class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")


class Bat(Mammal, WingedAnimal):
    pass


# create an object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()

# !multilevel inheritance syntax: derive a class from the derived class
class SuperClass:
    # Super class code here
    pass

class DerivedClass1(SuperClass):
    # Derived class 1 code here
    pass

class DerivedClass2(DerivedClass1):
    # Derived class 2 code here
    pass

# !e.g., 


class SuperClass:

    def super_method(self):
        print("Super Class method called")

# define class that derive from SuperClass


class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")

# define class that derive from DerivedClass1


class DerivedClass2(DerivedClass1):

    def derived2_method(self):
        print("Derived class 2 method called")


# create an object of DerivedClass2
d2 = DerivedClass2()

d2.super_method()  # Output: "Super Class method called"

d2.derived1_method()  # Output: "Derived class 1 method called"

d2.derived2_method()  # Output: "Derived class 2 method called"


# !Method Resolution Order (MRO) in Python
'''
If two superclasses have the same method name and the derived class calls that method, Python uses the MRO to search for the right method to call.

In this case, the MRO specifies that methods should be inherited from the leftmost superclass first, so info() of SuperClass1 is called rather than that of SuperClass2.
'''


class SuperClass1:
    def info(self):
        print("Super Class 1 method called")


class SuperClass2:
    def info(self):
        print("Super Class 2 method called")


class Derived(SuperClass1, SuperClass2):
    pass

# method resolution order MRO == leftmost superclass first
d1 = Derived()
d1.info()

# Output: "Super Class 1 method called"
