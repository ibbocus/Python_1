# Python program to
# demonstrate private methods

# Creating a Base class
class Parent:

# Declaring public method
    def public(self):
        print("Public method")

 # Declaring private method


    def __private(self):
        print("Private method")

    def call_private(self):
        print("private method inside parent class")
        self.__private()


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)

    def call_private(self):
        # Calling private method of Parent class
        self.__private()

    def call_public(self):
        print("inside child class")
        self.public()

parent_instance = Parent()
child_instance = Child()

#
parent_instance.call_private()
# #
#
child_instance.call_private()
# parent_instance.public()
