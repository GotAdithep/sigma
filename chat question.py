class Animal:
    def __init__(self, name="Unknown", species="Unknown"):
        self.__name = name  # Private attribute
        self.__species = species  # Private attribute

    # Getter and Setter for name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    # Getter and Setter for species
    def get_species(self):
        return self.__species
    def set_species(self, species):
        self.__species = species

    # Generic speak method
    def speak(self):
        print("Animal sound")

    # String representation
    def __str__(self):
        return f"Name: {self.__name}, Species: {self.__species}"

# Subclass Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name="Unknown", species="Dog", breed="Unknown"):
        super().__init__(name, species)  # Initialize the parent class
        self.__breed = breed  # Private attribute

    # Getter and Setter for breed
    def get_breed(self):
        return self.__breed
    def set_breed(self, breed):
        self.__breed = breed

    # Override speak method
    def speak(self):
        print("Woof!")

    # String representation
    def __str__(self):
        return super().__str__() + f", Breed: {self.__breed}"
