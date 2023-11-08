"""
The class Animal is a superclass for different animals in our case it is the superclass for the classes Cat and Dog.

The superclass contains the following:

    1. A constructor to initialize new instances of Animal.
    2. A method that is meant to be over-rided in the subclasses. 
"""


class Animal: ## Superclass

    def __init__(self, animal_type): ## Constructor
        self._type = animal_type

    def greets(self): ## Method meant to be over-rided in the subclasses
        raise NotImplementedError("Subclasses should implement this method")

"""
The class Cat is a subclass of the Animal superclass, meaning that it inherits from the superclass.

The subclass contains the following:

    1. A method that outputs the greetings of a Cat.
"""

class Cat(Animal): ## Subclass which inherits from the superclass

    def greets(self): ## Overriding method from superclass
        print("meow")

"""
The class Dog is a subclass of the Animal superclass, meaning that it inherits from the superclass.

The subclass contains the following:

    1. A constructor which inherits the the Animal class constructor by calling "super().__init__(animaltype)".
    A new attribute "size" is also added such that we now can specify both the animal and if it is a dog whether it is big or normal.
    2. A method that outputs the greeting of a dog based on the size of the dog.
"""

class Dog(Animal): ## Subclass which inherits from the superclass

    def __init__(self, animal_type, size="normal"): ## Inherits the constructor and added a new attribute "size"
        super().__init__(animal_type)
        self.size = size

    def greets(self): ## Overriding method from the superclass
        if self.size.lower() == "big":
            print("woof")
            print("woooof")
        else:
            print("woof")


## Test 
cat = Cat("Cat")
normal_sized_dog = Dog("Dog")
big_sized_dog = Dog("Big Dog", size="big")

cat.greets()
normal_sized_dog.greets()
big_sized_dog.greets()
